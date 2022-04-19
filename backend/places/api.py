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

class PostAPI(generics.GenericAPIView):
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.filter(username=request.user).first()
        print(user)
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
    
    def findPlaces(self, request, *args, **kwargs):
        print(request)
        posts = Post.objects.filter(username=request.user).all()
        return Response(posts)

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
        print("województwo " + str(self.request.query_params.get('state')))
        state = "województwo " + str(self.request.query_params.get('state'))
        posts = Post.objects.filter(state=state)
        return posts

    # Metoda wybiera z jakiego serializera będziemy korzystać
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)