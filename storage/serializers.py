from rest_framework import serializers
from .models import LinkStorage, Topic

class LinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = LinkStorage
        fields = ('id', 'topic', 'name', 'author', 'url', 'visited', 'note',)


class TopicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name')