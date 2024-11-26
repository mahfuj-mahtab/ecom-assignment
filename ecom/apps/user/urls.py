from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path("register/",  registerView.as_view(),name = 'registration view'),
    path("login/",  loginView.as_view(),name = 'Login view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]