"""functionality of the blog with Post class
Returns:
    _type_: _description_
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """Object representing user interface for post.

    Args:
        models (_type_): title, content, date_posted, author
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title