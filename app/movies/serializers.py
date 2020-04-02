"""

"""

from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Movie Serializer
    """

    class Meta:
        """
        Meta class for serializer defines the Serializer model and fields
        """

        model = Movie
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
