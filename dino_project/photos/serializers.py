from rest_framework import serializers
from.models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'bio']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'image_url', 'caption']

    def create(self, validated_data):
        #handle image upload separately if necessary
        return Post.objects.create(**validated_data)