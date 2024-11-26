from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
    path("admin/category/", AdminCategoryView.as_view(), name="category"),
    path("admin/product/", AdminProductView.as_view(), name="product"),
]
