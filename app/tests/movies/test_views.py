import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    """
    Sanity add movie test
    """
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        f"/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    """
    Empty POST data request
    """
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        f"/api/movies/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    """
    Data is not complete
    """
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        f"/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    """
    Get single existing Movie
    """
    # Create a Movie in the DB
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")

    # Request the Movie using the API
    resp = client.get(f"/api/movies/{movie.id}/")

    # Assert the response
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


@pytest.mark.django_db
def test_get_single_movie_incorrect_id(client):
    """
    Try to get none-existing movie from DB
    """
    resp = client.get(f"/api/movies/{30}/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    movie_two = add_movie("No Country for Old Men", "thriller", "2007")
    resp = client.get(f"/api/movies/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == movie_one.title
    assert resp.data[1]["title"] == movie_two.title
