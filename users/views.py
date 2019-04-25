from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser

class UserListView(generics.ListCreateAPIView):

	serializer_class = CustomUserSerializer

	queryset = CustomUser.objects.all()