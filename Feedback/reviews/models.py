from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    review_text = models.TextField(max_length=200, null= False)
    rating = models.IntegerField()