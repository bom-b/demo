from django.urls import path

from address import views

# request => address/write => views.writeForm() 호출
urlpatterns = [
    path('write',views.writeForm),
    path('insert',views.insert),
    path('list',views.addList),
    path('detail',views.detail),
    path('update',views.update),
    path('delete',views.delete),
]