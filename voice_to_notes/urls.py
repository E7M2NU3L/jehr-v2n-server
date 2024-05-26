# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from voice_to_notes.views import NotesViewSet

router = DefaultRouter()
router.register(r'notes', NotesViewSet, basename='note')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
