from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Blog, Post, Note, Multimedia, InteractiveContent, Review, Comment, UserGeneratedContent, SocialMediaPost, Advertisement, Widget, ResourceList, CallToAction
from django.contrib.auth.models import User

class APITestBase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

class BlogTests(APITestBase):

    def test_create_blog(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('blog-list')
        data = {'title': 'Test Blog', 'description': 'Blog description', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PostTests(APITestBase):

    def setUp(self):
        super().setUp()
        self.blog = Blog.objects.create(title='Test Blog', description='Blog description', author=self.user)

    def test_create_post(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('post-list')
        data = {'title': 'Test Post', 'description': 'Post description', 'author': self.user.id, 'blog': self.blog.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Similar tests can be written for other models like Note, Multimedia, etc.
class NoteTests(APITestBase):

    def test_create_note(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('note-list')
        data = {'title': 'Test Note', 'description': 'Note description', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class MultimediaTests(APITestBase):

    def test_create_multimedia(self, request):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('multimedia-list')
        data = {'file': request.file , 'media_type': 'image'}  # Add your file here
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class InteractiveContentTests(APITestBase):

    def test_create_interactive_content(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('interactivecontent-list')
        data = {'interaction_type': 'poll', 'data': {'question': 'Your question here', 'options': ['Option 1', 'Option 2']}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReviewTests(APITestBase):

    def test_create_review(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('review-list')
        data = {'review_text': 'This is a review', 'rating': 4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CommentTests(APITestBase):

    def test_create_comment(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('comment-list')
        data = {'text': 'This is a comment', 'user': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserGeneratedContentTests(APITestBase):

    def test_create_user_generated_content(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('ugc-list')
        data = {'title': 'User Generated Content', 'description': 'Description', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SocialMediaPostTests(APITestBase):

    def test_create_social_media_post(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('socialmediapost-list')
        data = {'platform': 'Twitter', 'post_url': 'https://twitter.com/example'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AdvertisementTests(APITestBase):

    def test_create_advertisement(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('advertisement-list')
        data = {'ad_type': 'affiliate', 'ad_content': 'Advertisement content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WidgetTests(APITestBase):

    def test_create_widget(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('widget-list')
        data = {'widget_type': 'search_bar', 'configuration': {'placeholder': 'Search'}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ResourceListTests(APITestBase):

    def test_create_resource_list(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('resourcelist-list')
        data = {'title': 'Resource List', 'description': 'Description', 'author': self.user.id, 'resources': ['Resource 1', 'Resource 2']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CallToActionTests(APITestBase):

    def test_create_call_to_action(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('cta-list')
        data = {'cta_text': 'Call to Action', 'target_url': 'https://example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
