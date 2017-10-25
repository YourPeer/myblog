from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import datetime
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug = models.AutoField(primary_key=True)
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-pub_date',)
    def __unicode__(self):
        return self.title
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
class Comment(models.Model):
    comment=models.CharField(max_length=200)
    comment_time=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-comment_time',)
    def __unicode__(self):
        return self.comment