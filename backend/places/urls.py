from django.urls import path
from django.urls.conf import path, include
from .api import PostAPI, PostsViewSet, AttachmentsViewSet, CommentsViewSet, PostsByLocalizationViewSet, PostViewSet
from knox import views as knox_views
from rest_framework import routers

router = routers.DefaultRouter()
# User
router.register('places', PostsViewSet)
router.register('postretive', PostViewSet)
router.register('placesbylocalization', PostsByLocalizationViewSet)
router.register('attachments', AttachmentsViewSet)
router.register('comments', CommentsViewSet)

urlpatterns = [
    path('api/post', PostAPI.as_view()),
    path('api/post/<int:pk>/', PostAPI.as_view()),
    path('api/', include(router.urls)),
]
