from django.urls import path

from resnet1 import views

urlpatterns = [
    path('resnet1_form', views.resnet1_writer),
    path('resnet1_insert', views.resnet1_insert),
]