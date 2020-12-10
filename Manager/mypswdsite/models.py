from django.db import models
# from django import forms
# Create your models here.
class Passwords(models.Model):
    website = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    username = models.CharField(max_length=60)

    def __str__(self):
        return self.website

