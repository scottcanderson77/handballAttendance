from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class report(models.Model):
    title = models.CharField(unique=True, max_length=200, default="title")
    timestamp = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=30)
    detailed_description = models.CharField(max_length=200)
    is_private = models.BooleanField(default="False")
    location = models.CharField(max_length=100, default="Virginia")
    is_encrypted = models.BooleanField(default="False")
    # document = models.FileField(default='document',upload_to='documents/')
    username_id = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.title

class Document(models.Model):
    document = models.FileField(default='document',upload_to='documents/')
    report_document = models.ForeignKey(report, on_delete=models.CASCADE)



class folder(models.Model):
    title = models.CharField(max_length=200, unique=True)
    added_reports = models.ManyToManyField(report)
    username_id = models.ForeignKey(User, null=True, blank=True)
    def __str__(self):
        return self.title
