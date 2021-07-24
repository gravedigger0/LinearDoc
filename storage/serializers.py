from rest_framework import serializers
from .models import LinkStorage

class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkStorage
        fields = ('id', 'topic', 'name', 'author', 'url', 'visited', 'note',)