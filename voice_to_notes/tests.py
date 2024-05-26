# myapp/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from voice_to_notes.models import V2NModel

class NotesAPITestCase(APITestCase):

    def setUp(self):
        self.note1 = V2NModel.objects.create(notes_title="Test Note 1", notes_content="Content for test note 1")
        self.note2 = V2NModel.objects.create(notes_title="Test Note 2", notes_content="Content for test note 2")
        self.create_url = reverse('note-list')
        self.detail_url = lambda id: reverse('note-detail', kwargs={'pk': id})

    def test_create_note(self):
        data = {
            "notes_title": "Test Note 3",
            "notes_content": "Content for test note 3"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(V2NModel.objects.count(), 3)
        self.assertEqual(V2NModel.objects.get(id=3).notes_title, "Test Note 3")

    def test_get_all_notes(self):
        response = self.client.get(self.create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_note(self):
        response = self.client.get(self.detail_url(self.note1.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['notes_title'], self.note1.notes_title)

    def test_update_note(self):
        data = {
            "notes_title": "Updated Test Note 1",
            "notes_content": "Updated content for test note 1"
        }
        response = self.client.put(self.detail_url(self.note1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note1.refresh_from_db()
        self.assertEqual(self.note1.notes_title, "Updated Test Note 1")

    def test_delete_note(self):
        response = self.client.delete(self.detail_url(self.note1.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(V2NModel.objects.count(), 1)
