from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# data in templates
def login(request):
    if request.method == "GET":
        name ="jasim"
        return render(request, 'login.html', {"data": name})   # Using dictionary
    elif request.method == "POST":
        print(request.POST)
        return HttpResponse("U are in")

def data(request):
    detail={"name": "jasim", "age": 20}
    details=[{"name": "Anas", "age": 20}, {"name": "Ankas", "age": 21}, {"name": "mammed", "age": 22}]
    values=None
    return render(request, 'data.html', {"det": detail, "dets": details, "val": values})

# form submision (GET, POST)
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        print(request.POST)     # gives the console output
        return HttpResponse("<h2>Submitted</h2>""<br>Firstname :"+request.POST.get('fname')+"<br>Lastname :"+request.POST.get('lname'))
    
def home(request):
    return render(request,"index.html")