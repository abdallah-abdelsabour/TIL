from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound 

# Create your views here.


# all products here 
def index(request):
    return HttpResponse("all product here ")
# products detils 
def product_details(request,id):
    return HttpResponse(f"product details")

