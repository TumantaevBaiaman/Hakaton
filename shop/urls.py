from django.urls import path, include
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    # PostCreateAPIView,
    # PostDetailAPIView,
    # PostUpdateAPIView,
    # PostDeleteAPIView
)

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
]