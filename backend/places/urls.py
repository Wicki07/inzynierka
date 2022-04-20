from django.urls import path
from django.urls.conf import path, include
from .api import PostAPI, PostsViewSet, AttachmentsViewSet
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
# User
router.register('places', PostsViewSet)
router.register('attachments', AttachmentsViewSet)

urlpatterns = [
    path('api/post', PostAPI.as_view()),
    path('api/', include(router.urls)),
]
