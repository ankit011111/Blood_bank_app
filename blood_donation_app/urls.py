from django.contrib import admin
from django.urls import path
from blood_donation_app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.home,name='home'),
    path('benifits',views.benifits,name='benifits'),
    path('donate_blood',views.donate_blood,name='donate_blood'),
    path('purchase_blood',views.purchase_blood,name='purchase_blood'),
    path('aboutus',views.aboutus,name='aboutus'),
]