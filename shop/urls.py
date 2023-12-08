from django.urls import path, include

from shop import views

urlpatterns = [
    path('write', views.product_write),
    path('insert', views.product_insert),
    path('list', views.product_list),
    path('detail', views.product_detail),
    path('update', views.product_update),
    path('update_img', views.product_update_img),
    path('delete', views.product_delete),
]