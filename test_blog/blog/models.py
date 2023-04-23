"""functionality of the blog with Post class
Returns:
    _type_: _description_
"""
import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from actstream.models import Action


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
    

class Feed(models.Model):
    """
    Feed provides Feed stream functionality

    Args:
        models (models.Model instance): django.db object

    Returns:
        str: content of feed
    """
    user = Profile.user
    content = models.CharField(max_length=360)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

        def __str__(self) -> str:
            return self.content
    
    @staticmethod
    def get_feed_stream(user, offset=0, limit=10):
        """Return a paginated feed stream for the given user."""

        actions = Action.objects.filter(actor_object_id=user.id)
        feed_stream = actions[offset:offset + limit]
        return feed_stream
