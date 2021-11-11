from django.db import models

class Users(models.Model):

    name                    = models.CharField(max_length=100)
    email                    = models.CharField(max_length=50)
    phone_number                = models.TextField(max_length=10)
    password                  = models.CharField(max_length=50)

class normusers(models.Model):

    name                    = models.CharField(max_length=100)
    email                    = models.CharField(max_length=50)
    phone_number                = models.TextField(max_length=10)
    password                  = models.CharField(max_length=50)
