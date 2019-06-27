from django.db import models
from django.utils import timezone

from .models import Post
admin.site.register(POST)

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    #objects = models.Manager()
    
    def summary(self):
        return self.body[:100] #pylint: disable=E1136

class Comment(models.Model):
    post = models.ForeignKey('Blog',on_delete = models.CASCADE,related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)        
