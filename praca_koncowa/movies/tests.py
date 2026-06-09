from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Director, Movie


class MovieViewSetCRUDTests(APITestCase):
    """Testy CRUD dla MovieViewSet."""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.director = Director.objects.create(
            name_surname="George Lucas",
            actor_image="movies/directors/director_1_DoLqWPO.jpg",
        )

        self.movie = Movie.objects.create(
            title="Star Wars",
            content="Film sci fi",
            release_date="1977-05-25",
            poster="movies/posters/poster_1_mUYoVy0.jpg",
            director=self.director,
        )

    def tearDown(self):
        Movie.objects.all().delete()
        Director.objects.all().delete()

    def test_movies_list_returns_200(self):
        # Test 1: Sprawdza tylko czy działa (kod 200)
        response = self.client.get("/api/movies/")
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_list_returns_correct_fields(self):
        # Test 2: Sprawdza obecność pól oraz poprawność ID w filmie
        response = self.client.get("/api/movies/")
        movie_data = response.data[0]
        
        # Sprawdzanie kluczy
        self.assertIn("id", movie_data)
        self.assertIn("title", movie_data)
        self.assertIn("content", movie_data)
        self.assertIn("release_date", movie_data)
        self.assertIn("poster", movie_data)
        self.assertIn("director", movie_data)
        self.assertIn("genre", movie_data)
        self.assertIn("actor", movie_data)

        self.assertEqual(movie_data["id"], self.movie.id)