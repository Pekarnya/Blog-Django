from django.contrib import admin
from .models import Post, Profile, Feed
from user_api.models import News


# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Feed)
admin.site.register(News)
