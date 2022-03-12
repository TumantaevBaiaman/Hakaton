import json
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from .serializers import PostSerializers
from rest_framework.generics import ListAPIView
from .models import Post
from django.shortcuts import get_object_or_404

# CreateModelMixin ---- POST method
# UpdateModelMixin ---- PUT method
# DestroyModelMixin ---- DELETE method


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class PostAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PostDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)


class PostListAPIView(
        mixins.CreateModelMixin,
        generics.ListAPIView
        ):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    serializer_class = PostSerializers
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Post.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
