from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import UserViewSet, PostViewSet, create_post

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/posts/', create_post, name='create_post'),
]
