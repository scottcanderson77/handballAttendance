from django.db import models
from django.contrib.auth.models import User, Group
from reports.models import *



# Create your models here.
class GroupReports(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    report_document = models.ForeignKey(report, on_delete=models.CASCADE, null=True, blank=True)
