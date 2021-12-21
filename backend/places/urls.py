from django.urls import path
from django.urls.conf import path, include
from .api import PostAPI
from knox import views as knox_views

urlpatterns = [
    path('api/post', PostAPI.as_view()),
]
