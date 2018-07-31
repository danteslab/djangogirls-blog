from django.contrib import admin

from .models import Post

# Registra el modelo en Django admin
admin.site.register(Post)