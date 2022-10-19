from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # If topic is deleted, set topic to null
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # Takes a time stamp with every update
    creatd = models.DateTimeField(auto_now_add=True) # Time stamp when created
    

    class Meta:
        ordering = ['-updated', '-creatd']

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # Establishes relationship to room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # Takes a time stamp with every update
    creatd = models.DateTimeField(auto_now_add=True) # Time stamp when created


    def __str__(self) -> str:
        return self.body[0:50]
