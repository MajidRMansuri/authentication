from django.shortcuts import render,redirect
from django.views import View
from .form import RegistrationForm, Profile_Form
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'index.html')

class Registration(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request,'registration.html',{'form':form})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful")
            return redirect('login')
           
            # res.save()

        return render(request,'registration.html',{'form':form})

class Profile_edit(View):
    def get(self,request):
        form = Profile_Form()
        return render(request,'profile.html',{'form':form})
    def post(self,request):
        form = Profile_Form(request.POST)
        if form.is_valid():
            user = request.user
            print("User",user)
            locality = form.cleaned_data['locality']
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            res = Profile(locality=locality,country=country,state=state,city=city,zipcode=zipcode,user=user)
            res.save()
            return redirect('index')
        messages.success(request,"Login Successful")
        return render(request,'profile.html',{'form':form})
