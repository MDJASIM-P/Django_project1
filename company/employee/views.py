from django.shortcuts import render     # for templates
from django.http import HttpResponse    # for text response
# Create your views here.

def firstrequest(request):
    return HttpResponse("Hello world")

def secondrequest(request):
    return HttpResponse("This is second response")

# Responsing Templates
def home(request):
    return render(request,"home.html")

# data in templates
def empdetials(request):
    details=[{"name":"Jasim", "age":23, "phone":988946554},
             {"name":"Anas", "age":25, "phone":9889646516},
             {"name":"Mujeeb", "age":21, "phone":98894845946},
             {"name":"Mammed", "age":20, "phone":988946516145},
             {"name":"Hisham", "age":23, "phone":988956516}]
    return render(request, "employee_details.html",{"dets":details})