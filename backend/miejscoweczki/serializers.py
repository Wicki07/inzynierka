from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from . import models

import random
import string

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], is_active = False)
        generated_activate_key_size = 64
        generated_activate_key_chars = string.ascii_letters + string.digits
        generated_activate_key = ''.join(random.choice(generated_activate_key_chars) for _ in range(generated_activate_key_size))
        models.UserActivate.objects.create(user_id=user,activate_code=generated_activate_key)
        subject = 'Aktywacja konta w serwisie Dziennik.'
        message = render_to_string('mail/activate.html', {
            'user': user,
            'activate_link': 'http://localhost:8080/activate/' + generated_activate_key
        })
        email = EmailMultiAlternatives( subject, message, from_email='Dziennik', to=[user.email])
        email.mixed_subtype = 'related'
        email.attach_alternative(message, "text/html")
        email.send()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")    

class UsersActivatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # Dane jakie potrzebujemy pobrać o uzytkowniku
        fields = ['is_active']