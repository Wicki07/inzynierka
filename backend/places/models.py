from django.db import models
from django.contrib.auth.models import User
import json

def upload_path(instance, filename):
    return '/'.join(['posts',str(instance.post_id),filename])

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=False, default='')
    localization = models.CharField(max_length=200, blank=False, default='')
    title = models.CharField(max_length=200, blank=False, default='')
    street = models.CharField(max_length=200, blank=True, default='')
    city = models.CharField(max_length=200, blank=True, default='')
    post_code = models.CharField(max_length=200, blank=True, default='')
    state = models.CharField(max_length=200, blank=True, default='')
    country = models.CharField(max_length=200, blank=True, default='')
    category = models.CharField(max_length=200, blank=False, default='')
    ratings = models.FloatField(null=True, blank=True, default=0.0)
    ratings_amount = models.IntegerField(blank=True, null=True,  default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def delete(self):
        self.image.delete()
        super(Attachment, self).delete()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, default='')
    parent_com = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    @property
    def child_comments(self):
        comments = Comment.objects.filter(parent_com=self.id)
        return comments