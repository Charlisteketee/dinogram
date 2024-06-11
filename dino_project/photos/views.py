from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from.models import User, Post
from.serializers import UserSerializer, PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):
    data = request.data.copy()
    data['user'] = request.user.id
    print(request.data)  # Debugging line
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)  # Debugging line
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Add the index view function to serve the React app
def index(request):
    return render(request, 'index.html')


