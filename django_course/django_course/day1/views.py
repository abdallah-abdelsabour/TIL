from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
  return render(request , 'product_home_page' )

def product_details(request , id):
  return HttpResponse("done ")