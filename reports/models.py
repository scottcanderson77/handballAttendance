from django.db import models

# Create your models here.
class report(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=30)
    detailed_description = models.CharField(max_length=200)
    is_public = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name