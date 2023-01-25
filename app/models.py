from django.db import models

# Create your models here.
class rev(models.Model):
    user_name=models.CharField(max_length=10)
    rating=models.IntegerField()
