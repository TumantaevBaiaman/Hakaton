from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from spake.permissions import IsOwnerOrReadOnly
from .serializers import (
    PostSerializersAnimal,
    PostSerializersVegetables,
    PostSerializersFruits,
    PostSerializersGround
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from .models import (
    PostGround,
    PostFruits,
    PostAnimal,
    PostVegetables
)


class PostListAPIViewGround(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = PostSerializersGround

    def get_queryset(self):
        r = self.request
        qs = PostGround.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIViewAnimal(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = PostSerializersAnimal

    def get_queryset(self):
        r = self.request
        qs = PostAnimal.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIViewFruits(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = PostSerializersFruits

    def get_queryset(self):
        r = self.request
        qs = PostFruits.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIViewVegetables(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = PostSerializersVegetables

    def get_queryset(self):
        r = self.request
        qs = PostVegetables.objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)