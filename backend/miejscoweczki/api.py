from rest_framework import generics, permissions, serializers, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.utils import serializer_helpers
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer, UsersActivatedSerializer
from .models import *
from django.contrib.auth import get_user_model

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UsersActivationAccountViewSet(generics.RetrieveAPIView):

    authentication_classes = []
    permission_classes = []

    serializer_class = UsersActivatedSerializer

    default_serializer_class = UsersActivatedSerializer
    
    def get_object(self):
        activation = UserActivate.objects.filter(activate_code=self.request.query_params.get('code'))
        user = get_user_model().objects.none()
        if(activation):
            user = [a.user_id for a in activation]
            # Aktywujemy konto użytkownika
            user[0].is_active = True
            user[0].save()
            # Usuwamy kod aktywacyjny
            activation.delete()
        return user