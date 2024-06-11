from django.urls import path
from .views import register, login_view, logout_view, CustomAuthToken


urlpatterns = [
  path('register/', register, name='register'),
  path('login/', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
  path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]