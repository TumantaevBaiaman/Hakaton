from django.contrib import admin
from .models import (
    PostGround,
    PostVegetables,
    PostFruits,
    PostAnimal
)

admin.site.register(PostGround)
admin.site.register(PostAnimal)
admin.site.register(PostFruits)
admin.site.register(PostVegetables)

# Register your models here.
