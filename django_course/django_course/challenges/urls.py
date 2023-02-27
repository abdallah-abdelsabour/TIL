
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("<int:month>" , views.month_number_handler,name='intpath'),
    path("<str:month>"  , views.monthHandler),
    path("" , views.index)]



