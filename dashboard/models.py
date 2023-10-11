from django.db import models

class Dealers(models.Model):
    name = models.CharField(max_length=255)
