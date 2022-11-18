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

    #Discover
    path('discover/', views.getDiscovers, name="Discovers"),
    path('discover/<str:pk>/', views.getDiscover, name="Discover"),


]
