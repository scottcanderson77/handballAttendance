from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class report(models.Model):
    title = models.CharField(max_length=200, default="title")
    timestamp = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=30)
    detailed_description = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    status_state=models.CharField(max_length=100, default="public")
    location = models.CharField(max_length=100, default="Virginia")
    is_encrypted = models.BooleanField(default=False)
    document = models.FileField(default='document',upload_to='documents/')
    uploaded_at = models.DateTimeField(default="9999-01-01")
    username_id = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.name
