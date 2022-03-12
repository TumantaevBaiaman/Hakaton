from rest_framework import serializers
from .models import (
    PostGround,
    PostFruits,
    PostAnimal,
    PostVegetables
)


class PostSerializersAnimal(serializers.ModelSerializer):
    class Meta:
        model = PostAnimal
        fields = [
            'user', 'content', 'timestamp'
        ]
        read_only_fields = ['user']


class PostSerializersGround(serializers.ModelSerializer):
    class Meta:
        model = PostGround
        fields = [
            'user', 'content', 'timestamp'
        ]
        read_only_fields = ['user']


class PostSerializersFruits(serializers.ModelSerializer):
    class Meta:
        model = PostFruits
        fields = [
            'user', 'content', 'timestamp'
        ]
        read_only_fields = ['user']


class PostSerializersVegetables(serializers.ModelSerializer):
    class Meta:
        model = PostVegetables
        fields = [
            'user', 'content', 'timestamp'
        ]
        read_only_fields = ['user']