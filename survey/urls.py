from django.urls import path

from survey import views

urlpatterns = [
    path('survey_list', views.serveyList),
    path('save_survey', views.save_survey),
    path('show_result', views.show_result)
]