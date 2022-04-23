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

class PostAPI(generics.GenericAPIView):
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        if (self.request.query_params.get('id')):
            id = self.request.query_params.get('id')
            posts = Post.objects.filter(id=id).first()
            serializer = PostSerializer(posts)
            return Response(serializer.data)
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
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

    def delete(self, request, *args, **kwargs):
        count = Post.objects.all().delete()
        return Response({'message': '{} Post został usunięty'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class PostsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
    # Lista serializerii dla danech typów zapytań
    serializer_classes = {
        'GET': PostSerializer,
    }

    # Jeżeli danego zapytania nie ma na liście serializer_classes to wykorzystany będzie domyślny
    default_serializer_class = PostSerializer
    
    # Metoda przygotowuje nam dane do zwrócenia - my potrzebujemy informacji o jednym użytkowniku
    def get_queryset(self):
        state = "województwo " + str(self.request.query_params.get('state'))
        posts = Post.objects.filter(state=state)
        return posts

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class AttachmentsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.none()
    
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
    
    def list(self, request):
        id = request.query_params.get('post')
        comments = Comment.objects.filter(post_id=id, parent_com=None)
        serializer = CommentSerializer(comments, many=True)
        print(serializer.data)
        return Response(serializer.data)


    def create(self, request):
        user = get_user_model().objects.filter(username=request.data['user']).first()
        Comment.objects.create(
            user_id=user.id, 
            post_id=request.data['post'],
            rate=request.data['rate'],
            comment=request.data['comment'],
            parent_com=request.data['parent_com'],
        )
        sum = 0
        amount = 0
        comments = Comment.objects.filter(post_id=request.data['post']).all()
        for comment in comments:
            if (comment.rate):
                amount += 1
                sum += comment.rate
        post = Post.objects.filter(id=request.data['post']).first()
        post.ratings = sum / amount
        post.ratings_amount = amount
        post.save()
        return Response(request.data)