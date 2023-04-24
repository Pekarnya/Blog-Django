from django.views.generic import ListView
from .models import News
from rest_framework import generics
from .serializers import NewsSerializer

# Create your views here.


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    