from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from chatapp.models import UserProfile, Messages

# serializing the 'Users' database for jason representation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('username', 'email')


# serializing the 'Messages' database

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Messages
        fields= ('room', 'sender')