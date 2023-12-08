from django.urls import path

from login import views

urlpatterns = [
    path('login', views.loginform),
    path('logout', views.logout),
]