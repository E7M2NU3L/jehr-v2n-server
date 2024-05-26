from rest_framework import viewsets
from .models import Blog, Post, Note, Multimedia, InteractiveContent, Review, Comment, UserGeneratedContent, SocialMediaPost, Advertisement, Widget, ResourceList, CallToAction
from .serializers import BlogSerializer, PostSerializer, NoteSerializer, MultimediaSerializer, InteractiveContentSerializer, ReviewSerializer, CommentSerializer, UserGeneratedContentSerializer, SocialMediaPostSerializer, AdvertisementSerializer, WidgetSerializer, ResourceListSerializer, CallToActionSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer

class InteractiveContentViewSet(viewsets.ModelViewSet):
    queryset = InteractiveContent.objects.all()
    serializer_class = InteractiveContentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserGeneratedContentViewSet(viewsets.ModelViewSet):
    queryset = UserGeneratedContent.objects.all()
    serializer_class = UserGeneratedContentSerializer

class SocialMediaPostViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaPost.objects.all()
    serializer_class = SocialMediaPostSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

class ResourceListViewSet(viewsets.ModelViewSet):
    queryset = ResourceList.objects.all()
    serializer_class = ResourceListSerializer

class CallToActionViewSet(viewsets.ModelViewSet):
    queryset = CallToAction.objects.all()
    serializer_class = CallToActionSerializer
