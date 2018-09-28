from django.shortcuts import render
from django.http import HttpRequest
from empdetails.models import Employee

# Create your views here.
def homepage(request):
    return render(request, "index.html", {})

def register(request):
    return render(request, "register.html", {})

def signin(request):
    return render(request, "signin.html", {})

def signup(request):
    if request.method == "POST":
        name = request.POST["fname"]
        dob = request.POST["dob"]
        emailid = request.POST["emailid"]
        contact = request.POST["contact"]

        emp = Employee(
            name = name,
            dob = dob,
            emailid = emailid,
            contact = contact
        )

        emp.save()

    return render(request, "index.html", {})