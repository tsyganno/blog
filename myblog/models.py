from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=200)
    weight_g = models.IntegerField()