from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=150)
    created_at = models.IntegerField()
    votes = models.IntegerField()


class Comment(models.Model):
    comment_author = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
