from django.db import models

# Create your models here.
class register_crime(models.Model):
    Location=models.CharField(max_length=200)
    Nearest_police_post=models.CharField(max_length=200)
    summary_of_crime=models.TextField()
    evidence=models.FileField()
