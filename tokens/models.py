from django.db import models

class Token(models.Model):
    token_id = models.DecimalField(max_digits=77, decimal_places=0)
    holder = models.CharField(max_length=42)

class Asset(models.Model):
    holder = models.CharField(max_length=42)
    balance = models.DecimalField(max_digits=77, decimal_places=0)
