# Generated by Django 4.1.3 on 2022-11-18 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('population', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
            ],
            options={
                'db_table': 'diseasetype',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(blank=True, max_length=40, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('cname', models.ForeignKey(blank=True, db_column='cname', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.country')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email', models.OneToOneField(blank=True, db_column='email', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.users')),
                ('degree', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('email', models.OneToOneField(blank=True, db_column='email', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.users')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'publicservant',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
                ('id', models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.diseasetype')),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('first_enc_date', models.DateField(blank=True, null=True)),
                ('cname', models.ForeignKey(blank=True, db_column='cname', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.country')),
                ('disease_code', models.ForeignKey(blank=True, db_column='disease_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.disease')),
            ],
            options={
                'db_table': 'discover',
            },
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('nid', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('id', models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.diseasetype')),
                ('email', models.ForeignKey(blank=True, db_column='email', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.doctor')),
            ],
            options={
                'db_table': 'specialize',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('total_deaths', models.IntegerField(blank=True, null=True)),
                ('total_patients', models.IntegerField(blank=True, null=True)),
                ('cname', models.ForeignKey(blank=True, db_column='cname', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.country')),
                ('disease_code', models.ForeignKey(blank=True, db_column='disease_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.disease')),
                ('email', models.ForeignKey(blank=True, db_column='email', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.publicservant')),
            ],
            options={
                'db_table': 'record',
            },
        ),
    ]