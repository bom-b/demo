from django.urls import path

from main import views

urlpatterns = [
    path('', views.mymain),
    path('error', views.error),
    path('keyboard', views.keyboard),
    path('picture_test', views.picture_test),
]