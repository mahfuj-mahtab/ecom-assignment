from django.contrib import admin
from django.urls import include, path
from .views import *
urlpatterns = [
    path("admin/category/", AdminCategoryView.as_view(), name="category"),
    path("admin/product/", AdminProductView.as_view(), name="product"),
    path("products/", ProductView.as_view(), name="product view"),
    path("products/single/<int:id>", SingleProductView.as_view(), name="Singleproduct view"),
    path("categories/", CategoryView.as_view(), name="Category view"),
]
