"""
Url patterns for API requests.

    This file contains the URL patterns
for the API application, which is independent
from the blog application. The URL patterns are
kept separately in this file.
"""

from django.urls import path
from .views import NewsList

urlpatterns = [
    path('api/news/', NewsList.as_view())
]
