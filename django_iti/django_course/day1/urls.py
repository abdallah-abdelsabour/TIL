
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name='products.home'),
    path('<int:id>' , views.product_details, name='products.details'),
    path('contact/' ,views.contact_us ,name="contact")

]