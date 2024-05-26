from rest_framework import serializers
from .models import Blog, Post, Note, Multimedia, InteractiveContent, Review, Comment, UserGeneratedContent, SocialMediaPost, Advertisement, Widget, ResourceList, CallToAction

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'

class InteractiveContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveContent
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserGeneratedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeneratedContent
        fields = '__all__'

class SocialMediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'

class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceList
        fields = '__all__'

class CallToActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToAction
        fields = '__all__'
