from django.db import models

# Create your models here.
class SiteSetting(models.Model):
    banner = models.ImageField(upload_to='banners/')
    caption=models.TextField()