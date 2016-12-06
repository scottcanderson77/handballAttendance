#in models.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from message.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    publicKey = models.CharField(max_length=1024)
    privateKey = models.CharField(max_length=1024, default=1)
    sentMessagesScene= models.IntegerField(default=0)
    recMessagesScene = models.IntegerField(default=0)
    isSuspended = models.BooleanField(default=False)

    def __str__(self):
          return "%s's profile" % self.user

