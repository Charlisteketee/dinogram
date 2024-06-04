from django.shortcuts import render
from rest_framework import viewsets
from.models import User, Post
from.serializers import UserSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Add the index view function to serve the React app
def index(request):
    return render(request, 'index.html')
