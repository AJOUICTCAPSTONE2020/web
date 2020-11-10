from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return [self.email,self.name, self.password]


class originalVid(models.Model):
  
    video_url=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    date=models.CharField(max_length=20)
    streamer=models.CharField(max_length=20)


class record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video= models.ForeignKey(originalVid, on_delete=models.CASCADE)
    create_date=models.CharField(max_length=20)

class chapter(models.Model):
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)
    chapter_name=models.CharField(max_length=30)
    start_time=models.IntegerField()
    end_time=models.IntegerField()

class highlightVid(models.Model):

    start_time=models.IntegerField()
    end_time=models.IntegerField()
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)

class chatFlow(models.Model):
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)
    time=models.IntegerField()
    num_of_chat=models.IntegerField()


class audioFlow(models.Model):
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)
    time=models.IntegerField()
    decibel=models.IntegerField()
  
class topWords(models.Model):
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)
    word=models.CharField(max_length=20)
    rank=models.IntegerField()
    appearance_time=models.IntegerField()


class sentiment(models.Model):
    video=models.ForeignKey(originalVid, on_delete=models.CASCADE)
    time=models.IntegerField()
    sentiment=models.CharField(max_length=20)

