from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieList(APIView):
    """

    """

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """

        :param request:
        :param format:
        :return:
        """
        serializer = MovieSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            raise e


class MovieDetail(APIView):
    """
    Retrieve a Movie
    """

    @staticmethod
    def get_object(pk):
        """
        Get the Object from the DB
        """
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """

        :return: Response with the Movie object serialized to it
        """
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class MoviesViewSet(ViewSet):
    """

    """
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_object(self, pk):
        """
        Get the Object from the DB
        """
        try:
            return self.model.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def list(self, request):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise e

    def retrieve(self, request, pk):
        movie = self.get_object(pk)
        serializer = self.serializer_class(movie)
        return Response(serializer.data)
