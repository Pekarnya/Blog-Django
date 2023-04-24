"""
 Transfers data into a format that is easy
 to consume over the internet. (JSON)
Displaying JSON at api endpoint
"""

from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields: tuple = ('theme', 'body', 'media_img', 'media_video')
