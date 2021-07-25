from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import LinkStorage, Topic
from .serializers import LinkSerializers, TopicSerializers

class LinkList(generics.ListCreateAPIView):
    queryset = LinkStorage.objects.all()
    serializer_class = LinkSerializers

class LinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkStorage.objects.all()
    serializer_class = LinkSerializers

class TopicName(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializers