from django.urls import path

from wordcnt import views

urlpatterns = [
    path('wordcntForm', views.word_cnt_form),
    path('wordcntProcess', views.word_cnt_process)
]