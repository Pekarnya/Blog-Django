from django.db import models

# Create your models here.


class News(models.Model):
    """
    Post stream model

    Reads the previous posts interface to RWD

    Args:
        models (Model instance): standart model from Django aplication
    """    """"""
    theme = models.CharField(max_length=35)
    body = models.TextField(max_length=500)
    media_img = models.ImageField(width_field='145px', height_field='145px')
    media_video = models.FileField()

    def __str__(self) -> str:
        return self.theme

