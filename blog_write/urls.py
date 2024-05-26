from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, PostViewSet, NoteViewSet, MultimediaViewSet, InteractiveContentViewSet, ReviewViewSet, CommentViewSet, UserGeneratedContentViewSet, SocialMediaPostViewSet, AdvertisementViewSet, WidgetViewSet, ResourceListViewSet, CallToActionViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'posts', PostViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'multimedia', MultimediaViewSet)
router.register(r'interactive-content', InteractiveContentViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ugc', UserGeneratedContentViewSet)
router.register(r'social-media-posts', SocialMediaPostViewSet)
router.register(r'advertisements', AdvertisementViewSet)
router.register(r'widgets', WidgetViewSet)
router.register(r'resource-lists', ResourceListViewSet)
router.register(r'ctas', CallToActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
