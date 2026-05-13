from django.test import TestCase
from django.core.cache import cache
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task, Place

# ============================================================
#  TESTY BEZ CACHE
# ============================================================


class TaskViewSetCRUDTests(APITestCase):
    """Testy CRUD dla TaskViewSet (ModelViewSet)."""

    def setUp(self):
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.anon_client = APIClient()
        self.task = Task.objects.create(
            title="Test task",
            description="Test description",
            completed=False,
        )

    def tearDown(self):
        cache.clear()

    # LIST

    def test_list_returns_200(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_returns_401_for_anon_client(self):
        response = self.anon_client.get("/api/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_returns_all_tasks(self):
        Task.objects.create(title="Second task", description="")
        response = self.client.get("/api/tasks/")
        self.assertEqual(len(response.data), 2)

    def test_list_returns_correct_fields(self):
        response = self.client.get("/api/tasks/")
        task_data = response.data[0]
        self.assertIn("id", task_data)
        self.assertIn("title", task_data)
        self.assertIn("description", task_data)
        self.assertIn("completed", task_data)
        self.assertIn("created_at", task_data)

    def test_list_ordered_by_created_at_descending(self):
        second = Task.objects.create(title="Second task", description="")
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.data[0]["id"], second.id)

    # RETRIEVE

    def test_retrieve_returns_200(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_returns_correct_task(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.data["title"], self.task.title)
        self.assertEqual(response.data["description"], self.task.description)

    def test_retrieve_nonexistent_task_returns_404(self):
        response = self.client.get("/api/tasks/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # CREATE

    def test_create_returns_201(self):
        payload = {"title": "New task", "description": "desc", "completed": False}
        response = self.client.post("/api/tasks/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_saves_to_database(self):
        payload = {"title": "New task", "description": "desc", "completed": False}
        self.client.post("/api/tasks/", payload)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_returns_created_object(self):
        payload = {"title": "New task", "description": "desc", "completed": False}
        response = self.client.post("/api/tasks/", payload)
        self.assertEqual(response.data["title"], payload["title"])

    def test_create_without_title_returns_400(self):
        payload = {"description": "brak tytułu", "completed": False}
        response = self.client.post("/api/tasks/", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_without_description_is_allowed(self):
        payload = {"title": "No desc task", "completed": False}
        response = self.client.post("/api/tasks/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # UPDATE (PUT)

    def test_update_returns_200(self):
        payload = {"title": "Updated", "description": "new desc", "completed": True}
        response = self.client.put(f"/api/tasks/{self.task.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_changes_data_in_database(self):
        payload = {"title": "Updated", "description": "new desc", "completed": True}
        self.client.put(f"/api/tasks/{self.task.id}/", payload)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated")
        self.assertTrue(self.task.completed)

    def test_update_nonexistent_task_returns_404(self):
        payload = {"title": "X", "description": "", "completed": False}
        response = self.client.put("/api/tasks/99999/", payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PARTIAL UPDATE (PATCH)

    def test_partial_update_returns_200(self):
        response = self.client.patch(
            f"/api/tasks/{self.task.id}/", {"title": "Patched"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_changes_only_sent_fields(self):
        self.client.patch(f"/api/tasks/{self.task.id}/", {"title": "Patched"})
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Patched")
        self.assertEqual(self.task.description, "Test description")  # niezmieniony

    def test_partial_update_completed_field(self):
        self.client.patch(f"/api/tasks/{self.task.id}/", {"completed": True})
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    # DELETE

    def test_delete_returns_204(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_removes_from_database(self):
        self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(len(Task.objects.filter(id=self.task.id)), 0)

    def test_delete_nonexistent_task_returns_404(self):
        response = self.client.delete("/api/tasks/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class PlaceListAndCreateViewTests(APITestCase):
    """Testy dla PlaceListAndCreateView (ListCreateAPIView)."""

    def setUp(self):
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.place = Place.objects.create(
            name="Kraków",
            description="Stare Miasto",
        )

    def tearDown(self):
        cache.clear()

    # LIST

    def test_list_returns_200(self):
        response = self.client.get("/api/places/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_returns_all_places(self):
        Place.objects.create(name="Warszawa", description="Centrum")
        response = self.client.get("/api/places/")
        self.assertEqual(len(response.data), 2)

    def test_list_returns_correct_fields(self):
        response = self.client.get("/api/places/")
        place_data = response.data[0]
        self.assertIn("id", place_data)
        self.assertIn("name", place_data)
        self.assertIn("description", place_data)
        self.assertIn("created_at", place_data)

    def test_list_ordered_by_created_at_descending(self):
        second = Place.objects.create(name="Gdańsk", description="Morze")
        response = self.client.get("/api/places/")
        self.assertEqual(response.data[0]["id"], second.id)

    # CREATE

    def test_create_returns_201(self):
        payload = {"name": "Wrocław", "description": "Rynek"}
        response = self.client.post("/api/places/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_saves_to_database(self):
        payload = {"name": "Wrocław", "description": "Rynek"}
        self.client.post("/api/places/", payload)
        self.assertEqual(Place.objects.count(), 2)

    def test_create_without_name_returns_400(self):
        payload = {"description": "brak nazwy"}
        response = self.client.post("/api/places/", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_without_description_is_allowed(self):
        payload = {"name": "Poznań"}
        response = self.client.post("/api/places/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_not_allowed_on_detail_endpoint(self):
        payload = {"name": "X", "description": "Y"}
        response = self.client.post(f"/api/places/{self.place.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class PlaceGetSingleViewTests(APITestCase):
    """Testy dla PlaceGetSingleView (RetrieveUpdateAPIView)."""

    def setUp(self):
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.place = Place.objects.create(
            name="Kraków",
            description="Stare Miasto",
        )

    def tearDown(self):
        cache.clear()

    # RETRIEVE

    def test_retrieve_returns_200(self):
        response = self.client.get(f"/api/places/{self.place.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_returns_correct_place(self):
        response = self.client.get(f"/api/places/{self.place.id}/")
        self.assertEqual(response.data["name"], "Kraków")
        self.assertEqual(response.data["description"], "Stare Miasto")

    def test_retrieve_nonexistent_place_returns_404(self):
        response = self.client.get("/api/places/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # UPDATE (PUT)

    def test_update_returns_200(self):
        payload = {"name": "Warszawa", "description": "Centrum"}
        response = self.client.put(f"/api/places/{self.place.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_changes_data_in_database(self):
        payload = {"name": "Warszawa", "description": "Centrum"}
        self.client.put(f"/api/places/{self.place.id}/", payload)
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, "Warszawa")
        self.assertEqual(self.place.description, "Centrum")

    def test_update_nonexistent_place_returns_404(self):
        payload = {"name": "X", "description": "Y"}
        response = self.client.put("/api/places/99999/", payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # PARTIAL UPDATE (PATCH)

    def test_partial_update_returns_200(self):
        response = self.client.patch(
            f"/api/places/{self.place.id}/", {"name": "Gdańsk"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_changes_only_sent_fields(self):
        self.client.patch(f"/api/places/{self.place.id}/", {"name": "Gdańsk"})
        self.place.refresh_from_db()
        self.assertEqual(self.place.name, "Gdańsk")
        self.assertEqual(self.place.description, "Stare Miasto")  # niezmieniony

    # DELETE — niedozwolone (RetrieveUpdate nie ma delete)

    def test_delete_not_allowed(self):
        response = self.client.delete(f"/api/places/{self.place.id}/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================================
#  TESTY Z CACHE
# ============================================================


class TaskViewSetCacheTests(APITestCase):
    """Testy cache dla TaskViewSet."""

    def setUp(self):
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            title="Test task",
            description="Test description",
        )

    def tearDown(self):
        cache.clear()

    def test_list_is_cached(self):
        self.client.get("/api/tasks/")
        # dodajemy obiekt z pominięciem API — cache nie jest czyszczony
        Task.objects.create(title="Hidden task", description="")
        response = self.client.get("/api/tasks/")
        self.assertEqual(len(response.data), 1)

    def test_cache_invalidated_after_create(self):
        self.client.get("/api/tasks/")
        self.client.post("/api/tasks/", {"title": "New task", "completed": False})
        response = self.client.get("/api/tasks/")
        titles = [t["title"] for t in response.data]
        self.assertIn("New task", titles)

    def test_cache_invalidated_after_update(self):
        self.client.get("/api/tasks/")
        self.client.patch(f"/api/tasks/{self.task.id}/", {"title": "Updated title"})
        response = self.client.get("/api/tasks/")
        titles = [t["title"] for t in response.data]
        self.assertIn("Updated title", titles)


class PlaceGetSingleViewCacheTests(APITestCase):
    """Testy cache dla PlaceGetSingleView."""

    def setUp(self):
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.place = Place.objects.create(
            name="Kraków",
            description="Stare Miasto",
        )

    def tearDown(self):
        cache.clear()

    def test_retrieve_populates_cache(self):
        cache_key = f"place_detail_{self.place.id}"
        self.client.get(f"/api/places/{self.place.id}/")
        self.assertIsNotNone(cache.get(cache_key))

    def test_cache_invalidated_after_put(self):
        cache_key = f"place_detail_{self.place.id}"
        self.client.get(f"/api/places/{self.place.id}/")
        self.assertIsNotNone(cache.get(cache_key))

        self.client.put(
            f"/api/places/{self.place.id}/", {"name": "Warszawa", "description": "X"}
        )
        self.assertIsNone(cache.get(cache_key))

    def test_cache_invalidated_after_patch(self):
        cache_key = f"place_detail_{self.place.id}"
        self.client.get(f"/api/places/{self.place.id}/")
        self.assertIsNotNone(cache.get(cache_key))

        self.client.patch(f"/api/places/{self.place.id}/", {"name": "Gdańsk"})
        self.assertIsNone(cache.get(cache_key))

    def test_retrieve_returns_fresh_data_after_update(self):
        self.client.get(f"/api/places/{self.place.id}/")
        self.client.patch(f"/api/places/{self.place.id}/", {"name": "Warszawa"})
        response = self.client.get(f"/api/places/{self.place.id}/")
        self.assertEqual(response.data["name"], "Warszawa")

    def test_cache_is_isolated_per_object(self):
        other_place = Place.objects.create(name="Gdańsk", description="Morze")
        cache_key_1 = f"place_detail_{self.place.id}"
        cache_key_2 = f"place_detail_{other_place.id}"

        self.client.get(f"/api/places/{self.place.id}/")
        self.client.get(f"/api/places/{other_place.id}/")

        # update tylko pierwszego obiektu
        self.client.patch(f"/api/places/{self.place.id}/", {"name": "Zmieniony"})

        self.assertIsNone(cache.get(cache_key_1))  # wyczyszczony
        self.assertIsNotNone(cache.get(cache_key_2))  # nienaruszony
