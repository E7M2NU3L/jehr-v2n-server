from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Common abstract base model for Title and Description
class BaseContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Model for Blogs
class Blog(BaseContent):
    pass

# Model for Posts
class Post(BaseContent):
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE)

# Model for Notes
class Note(BaseContent):
    pass

# Model for handling multimedia content
class Multimedia(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    file = models.FileField(upload_to='multimedia/')
    media_type = models.CharField(max_length=50)  # e.g., 'image', 'video', 'audio'

# Model for Interactive Content
class InteractiveContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    interaction_type = models.CharField(max_length=50)  # e.g., 'poll', 'quiz'
    data = models.JSONField()  # Store data like questions and options for polls/quizzes

# Model for Reviews
class Review(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # Assuming a rating out of 5 or 10

# Model for handling comments and discussions
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Model for User-Generated Content
class UserGeneratedContent(BaseContent):
    blog = models.ForeignKey(Blog, related_name='ugc', on_delete=models.CASCADE)

# Model for Social Media Integration
class SocialMediaPost(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    platform = models.CharField(max_length=50)  # e.g., 'Twitter', 'Facebook'
    post_url = models.URLField()

# Model for Advertising and Monetization
class Advertisement(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    ad_type = models.CharField(max_length=50)  # e.g., 'affiliate', 'sponsored'
    ad_content = models.TextField()

# Model for Widgets and Tools
class Widget(models.Model):
    blog = models.ForeignKey(Blog, related_name='widgets', on_delete=models.CASCADE)
    widget_type = models.CharField(max_length=50)  # e.g., 'search_bar', 'tag_cloud'
    configuration = models.JSONField()  # Store widget configuration settings

# Model for Resource Lists
class ResourceList(BaseContent):
    blog = models.ForeignKey(Blog, related_name='resources', on_delete=models.CASCADE)
    resources = models.JSONField()  # List of resources in JSON format

# Model for CTAs
class CallToAction(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    cta_text = models.CharField(max_length=200)
    target_url = models.URLField()
