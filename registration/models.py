#in models.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from message.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    publicKey = models.CharField(max_length=1024)
    privateKey = models.CharField(max_length=1024, default=1)
    practicesAttended= models.IntegerField(default=0)
    excusedAbsences= models.IntegerField(default=0)
    ATscore = models.FloatField(default=0)
    TimeLate = models.IntegerField(default=0)
    PP = models.IntegerField(default=0)
    isTeamMember = models.BooleanField(default=False)
    isOfficer = models.BooleanField(default=False)
    isSuspended = models.BooleanField(default=False)

    def __str__(self):
          return "%s's profile" % self.user

