
from django.urls import path , reverse 
from . import views





urlpatterns=[
    path('', views.index),
    path('id',views.product_details,id)
]



