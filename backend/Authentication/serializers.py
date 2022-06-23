from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from . import models
from django.utils.encoding import force_text
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
        subject = force_text('Aktywacja konta w serwisie Miejsca na 5.')
        from_mail = force_text('miejscoweczki@test.pl')
        message = render_to_string('mail/activate.html', {
            'user': user,
            'activate_link': 'http://localhost:8080/frontend/#/auth/activate/' + generated_activate_key
        })
        email = EmailMultiAlternatives( subject, message, from_mail, [user.email])
        email.mixed_subtype = 'related'
        email.attach_alternative(message, "text/html")
        email.send()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user :
            if user.is_active:  # added user model to OrderedDict that serializer is validating
                return user  # and in sunny day scenario, return this dict, as everything is fine
            raise serializers.ValidationError("Konto nie zostało aktywowane")
        raise serializers.ValidationError("Błędny login lub hasło") 

class UsersActivatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # Dane jakie potrzebujemy pobrać o uzytkowniku
        fields = ['is_active']