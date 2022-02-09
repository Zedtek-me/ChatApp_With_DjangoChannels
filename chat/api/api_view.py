from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, MessagesSerializer
from chatapp.models import UserProfile, Messages
from django.contrib.auth.models import User


def index(request):
    return render(request, 'api/index.html', {})

@api_view(['GET'])
def get_users(request):
    user= User.objects.all()
    serialized_users= UserSerializer(user, many= True)
    return Response(serialized_users.data)


@api_view(['GET'])
def get_messages(request):
    messages= Messages.objects.all()
    serialized_message= MessagesSerializer(messages, many= True)
    return Response(serialized_message.data)