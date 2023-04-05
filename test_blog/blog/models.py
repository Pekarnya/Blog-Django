"""functionality of the blog with Post class
Returns:
    _type_: _description_
"""
import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your models here.

user = get_user_model()


class Post(models.Model):
    """Object representing user interface for post.

    Args:
        models (_type_): title, content, date_posted, author
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    """Profile that represents a user profile class."""
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_user = models.BigIntegerField(null=True)
    unique_id = models.UUIDField(null=False, default=uuid.uuid4)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_img',
                                    default='basic_profile.jpg')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        """Username method

        Returns:
            str: Username info
        """
        return self.user.username
