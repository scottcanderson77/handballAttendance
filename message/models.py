from django.db import models
from django.contrib.auth.models import User, Group

from datetime import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Message(models.Model):
    message_title = models.CharField(max_length=50)
    message_body = models.CharField(max_length=500)
    #date = models.DateField(_("Time Sent"), default=datetime.today)
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")



    def __str__(self):
        return self.message_title



