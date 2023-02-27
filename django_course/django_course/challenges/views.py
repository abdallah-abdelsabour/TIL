from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound,HttpResponseRedirect
from  requests import get
from django.urls import reverse

# Create your views here.


# def get_all_products():
#     r= get(url='https://dummyjson.com/products')
#     data =r.json()
#     llist=[]
#     for l in data :
#       list.append(l)    
#     return llist



tsks={1:"hello", 2:"hello 2 ",3:"hellothreww",4:"hello4",5:"hello 5 ",6:"hello6",7:"hello 7 ",8:"hellofromhere"}


def index(request):
    return render(request,"index.html")



def month(request):
    return HttpResponse("month api ")

def monthHandler(request , month):
    
    return HttpResponse(f"request is string and eqal ")      

def month_number_handler(request, month):
    
    try:
        return HttpResponse(tsks[month])
    except:
        # t= reverse('intpath')
        # return HttpResponseRedirect(t)
         pass
    
    finally:
        return HttpResponse(f"requrst is numbers{month}")
    
    