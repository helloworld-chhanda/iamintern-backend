from django.db import models
from datetime import datetime   

# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title