from django.shortcuts import render,HttpResponseRedirect
from.models import *
from.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def home(request):
    obj=Student.objects.all().order_by('-date')
    return render(request, "index.html" ,{'obj': obj })


def student(request):
    obj = Student.objects.all().order_by('-date')
    if request.method=="POST":
        form=Student_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentform/')
    else:
        obj=Student.objects.all().order_by('-date')
        form=Student_form()
        return render(request, 'form.html', {'form':form,'obj': obj })

def registration(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            messages.success(request,' user registration succesfull')
            return HttpResponseRedirect('registration')

    else:
        form = UserForm()
        return render(request, 'registration.html', {'form': form})


def login(request):
    if request.method=="POST":
        username=request.POST['user']
        password=request.POST['pas']
        try:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return render(request,'welcome.html')
            else:
                messages.error(request,'username and password did not match')
        except auth.ObjectDoesNotExist:
            print("invalid user")
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
