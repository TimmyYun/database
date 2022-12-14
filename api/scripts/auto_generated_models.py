# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        db_table = 'diseasetype'


class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'country'


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING,
                           db_column='id', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'disease'


class Discover(models.Model):
    cname = models.ForeignKey(
        Country, models.DO_NOTHING, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(
        'Disease', models.DO_NOTHING, db_column='disease_code', blank=True, null=True, on_delete=models.CASCADE)
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'discover'


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(
        Country, models.DO_NOTHING, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'


class Publicservant(models.Model):
    email = models.ForeignKey(
        'Users', models.DO_NOTHING, db_column='email', blank=True, null=True, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'publicservant'


class Doctor(models.Model):
    email = models.ForeignKey(
        'Users', models.DO_NOTHING, db_column='email', blank=True, null=True, on_delete=models.CASCADE)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'doctor'


class Specialize(models.Model):
    id = models.ForeignKey(Diseasetype, models.DO_NOTHING,
                           db_column='id', blank=True, null=True, on_delete=models.CASCADE)
    email = models.ForeignKey(
        Doctor, models.DO_NOTHING, db_column='email', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'specialize'


class Record(models.Model):
    email = models.ForeignKey(
        Publicservant, models.DO_NOTHING, db_column='email', blank=True, null=True, on_delete=models.CASCADE)
    cname = models.ForeignKey(
        Country, models.DO_NOTHING, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(
        Disease, models.DO_NOTHING, db_column='disease_code', blank=True, null=True, on_delete=models.CASCADE)
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'record'
