from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    body_text = models.TextField()
    published_at = models.DateTimeField()
    author = models.ForeignKey(User)
