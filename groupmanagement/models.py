from django.db import models
from django.contrib.auth.models import User, Group
from reports.models import *


# Create your models here.
class GroupReports(models.Model):
    group = models.ManyToManyField(Group)
    report_document = models.ForeignKey(report, on_delete=models.CASCADE)
