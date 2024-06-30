from django.shortcuts import render , HttpResponse ,redirect
from datetime import datetime
from blood_donation_app.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"index.html")

def benifits(request):
    return render(request,"benifits.html")



def aboutus(request):
    return render(request,"aboutus.html")

def donate_blood(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        blood_group =request.POST.get('blood_group')
        gender =request.POST.get('gender')
        age =request.POST.get('age')
        address =request.POST.get('address')
        donate_blood = Donate_blood(name=name,email=email,phone=phone,blood_group=blood_group,gender=gender , age=age,address=address)
        donate_blood.save()
        
    
    return render(request,"donate_blood.html")

def purchase_blood(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        blood_group =request.POST.get('blood_group')
        gender =request.POST.get('gender')
        age =request.POST.get('age')
        address =request.POST.get('address')
        purchase_blood= Purchase_blood(name=name,email=email,phone=phone,blood_group=blood_group,gender=gender , age=age,address=address)
        purchase_blood.save()
        return render(request,"submitted.html")
    
        
    return render(request,"purchase_blood.html")