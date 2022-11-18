from django.db import models


class DiseaseType(models.Model):
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
    id = models.ForeignKey('DiseaseType', db_column='id',
                           blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'disease'


class Discover(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True,
                             serialize=True, verbose_name='ID', unique=True)
    cname = models.ForeignKey(
        Country, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(
        'Disease', db_column='disease_code', blank=True, null=True, on_delete=models.CASCADE)
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
        Country, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'users'


class PublicServant(models.Model):
    email = models.OneToOneField(
        'Users', db_column='email', blank=True, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'publicservant'


class Doctor(models.Model):
    email = models.OneToOneField(
        'Users', db_column='email', blank=True, on_delete=models.CASCADE, primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'doctor'


class Specialize(models.Model):
    nid = models.IntegerField(auto_created=True, primary_key=True,
                              serialize=True, verbose_name='ID', unique=True)
    id = models.ForeignKey(DiseaseType,
                           db_column='id', blank=True, null=True, on_delete=models.CASCADE)
    email = models.ForeignKey(
        Doctor, db_column='email', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'specialize'


class Record(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True,
                             serialize=True, verbose_name='ID', unique=True)
    email = models.ForeignKey(
        PublicServant, db_column='email', blank=True, null=True, on_delete=models.CASCADE)
    cname = models.ForeignKey(
        Country, db_column='cname', blank=True, null=True, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(
        Disease, db_column='disease_code', blank=True, null=True, on_delete=models.CASCADE)
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'record'
