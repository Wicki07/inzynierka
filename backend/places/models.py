from django.db import models
from django.contrib.auth.models import User

def upload_path(instance, filename):

    return '/'.join(['posts',str(instance.post_id.id),filename])

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=False, default='')
    localization = models.CharField(max_length=200, blank=False, default='')
    category = models.CharField(max_length=200, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate = models.IntegerField(blank=True, null=True)
    parent_com = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)