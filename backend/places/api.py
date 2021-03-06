from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from Authentication.serializers import UserSerializer
from .serializers import *
from .models import *
from rest_framework import status
from knox.auth import TokenAuthentication
from django.core.files import File
import urllib
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
import json
from django.http import JsonResponse
import math
import os

class PostAPI(generics.GenericAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def deleteFile(path):
        if os.path.isfile(path):
            os.remove(path)
       
    def post(self, request, *args, **kwargs):
        if (request.data.__contains__('id')):
            post = Post.objects.get(id=request.data['id'])
            post.localization=request.data['localization'] 
            post.title=request.data['title'] 
            post.description=request.data['description'] 
            post.street=request.data['street'] 
            post.city=request.data['city'] 
            post.post_code=request.data['post_code'] 
            post.state=request.data['state'] 
            post.country=request.data['country'] 
            post.category=request.data['category']
            for f in request.FILES.getlist('images'):
                Attachment.objects.create(post_id=post.id, image=f)
            for attachment in request.data['attachmentsToRemove']:
                att = Attachment.objects.get(id=attachment)
                att.delete()
            post.save()
            return Response({'message': '{} Post został zaktualizowany'}, status=status.HTTP_200_OK)
        else:
            user = get_user_model().objects.filter(username=request.user).first()
            post = Post.objects.create(
                user_id=user.id, 
                localization=request.data['localization'], 
                title=request.data['title'], 
                description=request.data['description'], 
                street=request.data['street'], 
                city=request.data['city'], 
                post_code=request.data['post_code'], 
                state=request.data['state'], 
                country=request.data['country'], 
                category=request.data['category']
            )
            for f in request.FILES.getlist('images'):
                Attachment.objects.create(post_id=post.id, image=f)
            return Response({'message': '{} Post został dodany'}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        Post.objects.get(id=pk).delete()
        return Response({'message': '{} Post został usunięty'}, status=status.HTTP_204_NO_CONTENT)

class PostsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    authentication_classes = []
    permission_classes = []
    
    # Lista serializerii dla danech typów zapytań
    serializer_classes = {
        'GET': PostsSerializer,
    }

    # Jeżeli danego zapytania nie ma na liście serializer_classes to wykorzystany będzie domyślny
    default_serializer_class = PostsSerializer
    
    def get_queryset(self):
        if self.request.query_params.get('state'):
            state = "województwo " + str(self.request.query_params.get('state'))
            posts = Post.objects.filter(state=state)
            for post in posts:
                post.attachments = Attachment.objects.filter(post_id=post.id)

        else:
            user = User.objects.get(username=self.request.query_params.get('user'))
            posts = Post.objects.filter(user_id=user.id)
            for post in posts:
                post.attachments = Attachment.objects.filter(post_id=post.id)
        return posts

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
class PostViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    authentication_classes = []
    permission_classes = []
    
    # Lista serializerii dla danech typów zapytań
    serializer_classes = {
        'GET': PostSerializer,
    }

    # Jeżeli danego zapytania nie ma na liście serializer_classes to wykorzystany będzie domyślny
    default_serializer_class = PostSerializer
    
    def get_queryset(self):
        id = self.request.query_params.get('id')
        post = Post.objects.filter(id=id)
        return post

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class PostsByLocalizationViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    authentication_classes = []
    permission_classes = []
    
    # Lista serializerii dla danech typów zapytań
    serializer_classes = {
        'GET': PostsSerializer,
    }

    # Jeżeli danego zapytania nie ma na liście serializer_classes to wykorzystany będzie domyślny
    default_serializer_class = PostsSerializer

    def calcCrow(self, _lat1, lon1, _lat2, lon2):
        R = 6371
        dLat = self.toRad(_lat2 - _lat1);
        dLon = self.toRad(lon2 - lon1);
        lat1 = self.toRad(_lat1);
        lat2 = self.toRad(_lat2);

        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));
        return R * c

    def toRad(self, Value):
        return (Value * math.pi) / 180

    def get_queryset(self):
        lat = str(self.request.query_params.get('lat'))
        lon = str(self.request.query_params.get('lon'))
        distance = float(str(self.request.query_params.get('distance')))
        returnPosts = []
        data = Post.objects.all()
        for post in data:
            postDistance = self.calcCrow(float(lat), float(lon), float(post.localization.split(",")[0]), float(post.localization.split(",")[1]))
            if(postDistance <= distance):
                returnPosts.append(post)
        for post in returnPosts:
            post.attachments = Attachment.objects.filter(post_id=post.id)
        return returnPosts

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class MainScreenPosts(generics.GenericAPIView):
    
    authentication_classes = []
    permission_classes = []
    
    def get(self, request):
        data = Post.objects.raw('SELECT p.id, p.state, COUNT(p.id) as count FROM places_post p GROUP BY p.state')
        serializer = MainsScreenPostsSerializer(data, many=True)
        return Response(serializer.data)

class AttachmentsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    authentication_classes = []
    permission_classes = []

    # Lista serializerii dla danech typów zapytań
    serializer_classes = {
        'GET': AttachmentSerializer,
    }
    # Jeżeli danego zapytania nie ma na liście serializer_classes to wykorzystany będzie domyślny
    default_serializer_class = AttachmentSerializer
    
    # Metoda przygotowuje nam dane do zwrócenia - my potrzebujemy informacji o jednym użytkowniku
    def get_queryset(self):
        id = self.request.query_params.get('post')
        attachments = Attachment.objects.filter(post_id=id)
        return attachments

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    serializer_class = CommentSerializer

    default_serializer_class = CommentSerializer
    authentication_classes = []
    permission_classes = []
    
    def list(self, request):
        id = request.query_params.get('post')
        comments = Comment.objects.filter(post_id=id, parent_com=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        if (request.data.__contains__('editedComment') and request.data['editedComment'] != None):
            comment = Comment.objects.get(id=request.data['editedComment'])
            comment.rate=request.data['rate']
            comment.comment=request.data['comment']
            comment.save()
            return Response(request.data)
        else:
            user = get_user_model().objects.filter(username=request.data['user']).first()
            Comment.objects.create(
                user_id=user.id, 
                post_id=request.data['post'],
                rate=request.data['rate'],
                comment=request.data['comment'],
                parent_com=None if request.data['parent_com'] == 0 else request.data['parent_com'],
            )
            sum = 0
            amount = 0
            comments = Comment.objects.filter(post_id=request.data['post']).all()
            for comment in comments:
                if (comment.rate):
                    amount += 1
                    sum += comment.rate
            post = Post.objects.filter(id=request.data['post']).first()
            post.ratings = sum / amount if amount != 0 else 0
            post.ratings_amount = amount
            post.save()
            return Response(request.data)

    def destroy(self, request, pk, format=None):
        deletedComment = Comment.objects.get(id=pk)
        postId = deletedComment.post_id
        deletedComment.delete()
        sum = 0
        amount = 0
        comments = Comment.objects.filter(post_id=postId).all()
        for comment in comments:
            if (comment.rate):
                amount += 1
                sum += comment.rate
        post = Post.objects.filter(id=postId).first()
        post.ratings = sum / amount if amount != 0 else 0
        post.ratings_amount = amount
        post.save()
        return Response({'message': '{} comment został usunięty'}, status=status.HTTP_204_NO_CONTENT)