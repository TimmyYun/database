from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    # DiseaseType
    path('diseasetype/', views.getDiseaseTypes, name="DiseaseTypes"),
    path('diseasetype/<str:pk>/', views.getDiseaseType, name="DiseaseType"),

    # Country
    path('country/', views.getCountries, name="Countries"),
    path('country/<str:pk>/', views.getCountry, name="Country"),

    # Disease
    path('disease/', views.getDiseases, name="Diseases"),
    path('disease/<str:pk>/', views.getDisease, name="Disease"),

    # Discover
    path('discover/', views.getDiscovers, name="Discovers"),
    path('discover/<str:pk>/', views.getDiscover, name="Discover"),

    # User
    path('user/', views.getUsers, name="Users"),
    path('user/<str:pk>/', views.getUser, name="User"),

    # PublicServant
    path('publicservant/', views.getPublicServants, name="PublicServants"),
    path('publicservant/<str:pk>/', views.getPublicServant, name="PublicServant"),

    # Doctor
    path('doctor/', views.getDoctors, name="Doctors"),
    path('doctor/<str:pk>/', views.getDoctor, name="Doctor"),

    # Specialize
    path('specialize/', views.getSpecializes, name="Specializes"),
    path('specialize/<str:pk>/', views.getSpecialize, name="Specialize"),

    # Record
    path('record/', views.getRecords, name="Records"),
    path('record/<str:pk>/', views.getRecord, name="Record"),

]
