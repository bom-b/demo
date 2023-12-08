from django.urls import path

from resapi import views

urlpatterns = [
    path('loadJsonTest1', views.loadJson),
    path('chartJson', views.chartJson),
    path('laodJsonp', views.loadJsonp),
    path('djangoAjax', views.gojango),
]