from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
# Create your views here.
class AdminCategoryView(APIView):
    # user must be admin to access this route
    permission_classes = [IsAdminUser]
    
    # this function fetch all the categories from the database
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
#    this function create a new category
    def post(self,request):

        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid(): # if the data is valid then we will create a new category
            serializer.save(created_by = request.user) # we will save the category with the user object
            return Response({'message': 'Category Created Successfully'},status=201)
        return Response({'message': 'Invalid Data'},status=403)
    # this function update a category
    def put(self,request):
        category = Category.objects.get(id = request.data['id'])
        serializer = CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid(): # if the data is valid then we will update the category
            serializer.save()
            return Response({'message': 'Category Updated Successfully'},status=201)
        return Response({'message': 'Invalid Data'},status=403)
    # this function delete a category
    def delete(self,request):
        category = Category.objects.get(id = request.data['id'])
        category.delete()
        return Response({'message': 'Category Deleted Successfully'},status=201)

class AdminProductView(APIView):

    # user must be admin to access this route
    permission_classes = [IsAdminUser]

    # this function fetch all the products from the database
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)   
        return Response({'products': serializer.data},status = 200)
  
    #    this function create a new product
    def post(self,request):
        try:
            category = Category.objects.get(id = request.data['category']) #checking if the category exist or not
        except Category.DoesNotExist:
            return Response({'message': 'Invalid Category'},status=403)
        try:
            user = User.objects.get(id = request.user.id) #checking if the user exist or not
        except User.DoesNotExist:
            return Response({'message': 'Invalid User'},status=403)
        product = Product(category = category,name = request.data['name'],description = request.data['description'],price = request.data['price'],image_url = request.data['image_url'],stock = request.data['stock'],created_by = user)
        product.save() #saving the product
        return Response({'message': 'Product Created Successfully'},status=201)
    #    this function update a product
    def put(self,request):
        product = Product.objects.get(id = request.data['id']) #fetching product from the database using product id
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid(): #if the data is valid then we will update the product
            serializer.save()
            return Response({'message': 'Product Updated Successfully'},status=201) 
        return Response({'message': 'Invalid Data'},status=403)
    def delete(self,request):
        product = Product.objects.get(id = request.data['id'])
        product.delete()
        return Response({'message': 'Product Deleted Successfully'},status=201)
    
class ProductView(APIView):
    #this function fetch all the products from the database
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)   
        return Response({'products': serializer.data},status = 200)


class SingleProductView(APIView):
    # this function fetch a single product from the database
    def get(self,request,id):
        product = Product.objects.get(id = id)
        serializer = ProductSerializer(product)   
        return Response({'product': serializer.data},status = 200)  

class CategoryView(APIView):
    # this function fetch all the categories from the database
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)   
        return Response({'categories': serializer.data},status = 200)   