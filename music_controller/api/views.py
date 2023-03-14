from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()           #what we wanna return
    serializer_class = RoomSerializer       #how to convert the data into a format that we can use
     
