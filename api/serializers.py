from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from api.models import *


class DiseaseTypeSerializer(ModelSerializer):
    class Meta:
        model = DiseaseType
        fields = '__all__'


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class DiscoverSerializer(ModelSerializer):
    class Meta:
        model = Discover
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class PublicServantSerializer(ModelSerializer):
    class Meta:
        model = PublicServant
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class SpecializeSerializer(ModelSerializer):
    class Meta:
        model = Specialize
        fields = '__all__'


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
