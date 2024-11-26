
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("v1/ecom/", include("apps.ecom.urls")),
    path("v1/users/", include("apps.user.urls")),
]
