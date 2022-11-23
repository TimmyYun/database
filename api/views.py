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
            'country/',
            'disease/',
            'discover/',
            'user/',
            'publicservant/',
            'doctor/',
            'specialize/',
            'record/'
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
        diseaseType = DiseaseType.objects.get(id=pk)
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
        country = Country.objects.get(cname=pk)
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
        disease = Disease.objects.get(id=pk)
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


# Discover


@api_view(['GET', 'POST'])
def getDiscovers(request):
    """
    List all discovers, or create a new discover.
    """
    if request.method == 'GET':
        discover = Discover.objects.all()
        serializer = DiscoverSerializer(discover, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DiscoverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getDiscover(request, pk):
    """
    Retrieve, update or delete a discover.
    """
    try:
        discover = Discover.objects.get(id=pk)
    except Discover.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiscoverSerializer(discover, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DiscoverSerializer(
            instance=discover, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        discover.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Users


@api_view(['GET', 'POST'])
def getUsers(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getUser(request, pk):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = Users.objects.get(id=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(user, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = UsersSerializer(
            instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# PublicServant


@api_view(['GET', 'POST'])
def getPublicServants(request):
    """
    List all public servants, or create a new public servant.
    """
    if request.method == 'GET':
        publicServant = PublicServant.objects.all()
        serializer = PublicServantSerializer(publicServant, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PublicServantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getPublicServant(request, pk):
    """
    Retrieve, update or delete a public servant.
    """
    try:
        publicServant = PublicServant.objects.get(id=pk)
    except PublicServant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PublicServantSerializer(publicServant, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PublicServantSerializer(
            instance=publicServant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        publicServant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Doctor


@api_view(['GET', 'POST'])
def getDoctors(request):
    """
    List all doctors, or create a new doctor.
    """
    if request.method == 'GET':
        doctor = Doctor.objects.all()
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getDoctor(request, pk):
    """
    Retrieve, update or delete a doctor.
    """
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DoctorSerializer(
            instance=doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Specialize


@api_view(['GET', 'POST'])
def getSpecializes(request):
    """
    List all specializes, or create a new specialize.
    """
    if request.method == 'GET':
        specialize = Specialize.objects.all()
        serializer = SpecializeSerializer(specialize, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SpecializeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getSpecialize(request, pk):
    """
    Retrieve, update or delete a specialize.
    """
    try:
        specialize = Specialize.objects.get(id=pk)
    except Specialize.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpecializeSerializer(specialize, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SpecializeSerializer(
            instance=specialize, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        specialize.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Record


@api_view(['GET', 'POST'])
def getRecords(request):
    """
    List all records, or create a new record.
    """
    if request.method == 'GET':
        record = Record.objects.all()
        serializer = RecordSerializer(record, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getRecord(request, pk):
    """
    Retrieve, update or delete a record.
    """
    try:
        record = Record.objects.get(id=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecordSerializer(record, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RecordSerializer(
            instance=record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

