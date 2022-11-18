from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from api.models import *
from api.serializers import *

# Routes


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'diseasetype/',
        }
    ]
    return Response(routes)

# Disease Type


@api_view(['GET', 'POST'])
def getDiseaseTypes(request):
    """
    List all disease types, or create a new disease type.
    """
    if request.method == 'GET':
        diseaseType = DiseaseType.objects.all()
        serializer = DiseaseTypeSerializer(diseaseType, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DiseaseTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getDiseaseType(request, pk):
    """
    Retrieve, update or delete a disease type.
    """
    try:
        diseaseType = DiseaseType.objects.get(pk=pk)
    except DiseaseType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiseaseTypeSerializer(diseaseType, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DiseaseTypeSerializer(
            instance=diseaseType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        diseaseType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Country


@api_view(['GET', 'POST'])
def getCountries(request):
    """
    List all countries, or create a new country.
    """
    if request.method == 'GET':
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getCountry(request, pk):
    """
    Retrieve, update or delete a country.
    """
    try:
        country = Country.objects.get(email=pk)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CountrySerializer(
            instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Disease


@api_view(['GET', 'POST'])
def getDiseases(request):
    """
    List all diseases, or create a new disease.
    """
    if request.method == 'GET':
        disease = Disease.objects.all()
        serializer = DiseaseSerializer(disease, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getDisease(request, pk):
    """
    Retrieve, update or delete a disease.
    """
    try:
        disease = Disease.objects.get(disease_code=pk)
    except Disease.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiseaseSerializer(disease, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DiseaseSerializer(
            instance=disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        disease.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
