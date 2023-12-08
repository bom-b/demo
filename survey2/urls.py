from django.urls import path

from survey2 import views

urlpatterns = [
    path('survey_list2', views.surveyList),
    path('save_survey2', views.save_survey),
    path('show_result2', views.show_result)
]