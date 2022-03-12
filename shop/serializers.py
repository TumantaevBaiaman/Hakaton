from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user', 'title', 'content', 'summa', 'contact', 'image', 'timestamp'
        ]
        read_only_fields = ['user']