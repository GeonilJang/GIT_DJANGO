from django.db import models

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
