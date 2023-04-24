from django.contrib import admin
from .models import Post, Profile, Feed


# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Feed)
