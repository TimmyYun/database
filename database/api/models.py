from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class DiseaseType(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True,
                             serialize=True, verbose_name='ID', unique=True)
    description = models.CharField(max_length=140)


class Country(models.Model):
    cname = models.CharField(max_length=50, primary_key=True)
    population = models.BigIntegerField()


class Disease(models.Model):
    dCode = models.CharField(max_length=50, primary_key=True)
    dType = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
