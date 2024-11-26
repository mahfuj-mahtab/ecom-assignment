from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


from .serializers import *
# Create your views here.
class registerView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
       
    #    checking if email is already exist  or not
        emails = User.objects.filter(email = email)
        if(len(emails) != 0):
            return Response({'message': 'Email already exists.'},status=403)
       
    #    checking is password length is correct or not 
        if(len(password) < 8 or len(password) > 64):
            return Response({'message': 'Enter A Valid Password'},status=403)
    #    checking if first name or last name is empty or not
        if(len(first_name) < 2 or len(last_name) < 2):
            return Response({'message': 'First name or Last name is invalid'},status=403)

        username = email.split("@")[0]
        user = User.objects.create_user(email = email,first_name = first_name,last_name = last_name,username = username,password = password)
        user.save()
        return Response({'message': 'User Registered Successfully'},status=201)

class loginView(APIView):
    def post(self,request):
        email = request.data['email']
        username = email.split("@")[0]
        password = request.data['password']
        user = authenticate(request,username = username,password = password)
        if(user is not None):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'message': 'Invalid Credentials'},status=403)
