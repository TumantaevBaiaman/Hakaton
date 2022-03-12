from django.urls import path
from .views import (
    PostListAPIViewAnimal,
    PostListAPIViewFruits,
    PostListAPIViewGround,
    PostListAPIViewVegetables
)


urlpatterns = [
    path('animal/', PostListAPIViewAnimal.as_view(), name='list'),
    path('vegetables/', PostListAPIViewVegetables.as_view(), name='list'),
    path('fruits/', PostListAPIViewFruits.as_view(), name='list'),
    path('ground/', PostListAPIViewGround.as_view(), name='list'),
]