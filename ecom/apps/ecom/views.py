from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
# Create your views here.
class AdminCategoryView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
    def post(self,request):

        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response({'message': 'Category Created Successfully'},status=201)
        return Response({'message': 'Invalid Data'},status=403)
    def put(self,request):
        category = Category.objects.get(id = request.data['id'])
        serializer = CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category Updated Successfully'},status=201)
        return Response({'message': 'Invalid Data'},status=403)
    def delete(self,request):
        category = Category.objects.get(id = request.data['id'])
        category.delete()
        return Response({'message': 'Category Deleted Successfully'},status=201)

class AdminProductView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)   
        return Response({'products': serializer.data},status = 200)
    def post(self,request):
        try:
            category = Category.objects.get(id = request.data['category'])
        except Category.DoesNotExist:
            return Response({'message': 'Invalid Category'},status=403)
        try:
            user = User.objects.get(id = request.user.id)
        except User.DoesNotExist:
            return Response({'message': 'Invalid User'},status=403)
        product = Product(category = category,name = request.data['name'],description = request.data['description'],price = request.data['price'],image_url = request.data['image_url'],stock = request.data['stock'],created_by = user)
        product.save()
        return Response({'message': 'Product Created Successfully'},status=201)
    def put(self,request):
        product = Product.objects.get(id = request.data['id'])
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product Updated Successfully'},status=201) 
        return Response({'message': 'Invalid Data'},status=403)
    def delete(self,request):
        product = Product.objects.get(id = request.data['id'])
        product.delete()
        return Response({'message': 'Product Deleted Successfully'},status=201)