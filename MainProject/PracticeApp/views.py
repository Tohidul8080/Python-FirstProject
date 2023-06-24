from django.shortcuts import render
from django.http import HttpResponse

from PracticeApp.models import Contact


# Create your views here.

def dasboard(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')
def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')
def contract(request):
    if request.method== "POST":
        name=request.POST['name']
        email = request.POST['email']
        Dsec=request.POST['Dsec']
        Values = Contact(name=name, email=email, Dsec=Dsec)
        Values.save()
    return render(request,'contract.html')










