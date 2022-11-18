from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),

    # DiseaseType
    path('diseasetype/', views.getDiseaseTypes, name="DiseaseTypes"),
    path('diseasetype/<str:pk>/', views.getDiseaseType, name="DiseaseType"),

    #Country
    path('country/', views.getCountries, name="Countries"),
    path('country/<str:pk>/', views.getCountry, name="Country"),


]
