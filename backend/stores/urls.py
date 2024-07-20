from django.urls import path
from . import views

urlpatterns = [
    path('api/create_geo_coordinate/', views.create_geo_coordinate, name='create geo coordinate')
]