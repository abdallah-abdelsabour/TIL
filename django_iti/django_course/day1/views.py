from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import requests
# Create your views here.


def get_all_products():
    r= requests.get(url='https://dummyjson.com/products')
    all =r.json()
    return(all['products'])
    
  
def get_product_by_id(id):
   products = get_all_products()
   for pro in products:
      if pro['id'] == id:
         return pro
      # print(pro['id'])
   return None


def index(request):
  all_products = get_all_products()
  # print(type (all_products))
  # print(all_products)

  return render(request,'products/index.html',context={'products':all_products} )


def product_details(request, id):
   pro= get_product_by_id(id)
   if pro :
      return render(request,"products/product.html",context={'pro':pro})
   else:
      return render(request,"products/404.html")
      
def contact_us(request):
   
   return render(request  ,"products/contact_us.html" )