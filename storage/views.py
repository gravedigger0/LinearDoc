from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import LinkStorage
from .serializers import LinkSerializers

class LinkList(generics.ListCreateAPIView):
    queryset = LinkStorage.objects.all()
    serializer_class = LinkSerializers

class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkStorage.objects.all()
    serializer_class = LinkSerializers

