from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from.models import User, Post
from.serializers import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# def add_mock_data(request):
#     mock_post = [
#         {"user": "deenasaurus", "image_url": "", "caption":""},
#         {"user": "tylerex", "image_url": "", "caption":""},
#         {"user": "tiny_triceritops", "": "", "caption":""},
#         {"user": "Bob", "image_url": "", "caption":""},
#         {"user": "DINO_Enthusiast", "image_url": "", "caption":""},
#         {"user": "NoNo", "image_url": "", "caption":""},
#     ]

# Add the index view function to serve the React app
def index(request):
    return render(request, 'index.html')


