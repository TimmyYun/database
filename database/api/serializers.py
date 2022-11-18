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