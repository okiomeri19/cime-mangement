
import re
from. forms import CreateUserForm
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required 
from .models import register_crime
# Create your views here.
def homepage(request):
	return render(request,'crime/homepage.html')
def register(request):
	form=CreateUserForm()
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Account was created for'+user)
			return redirect('login')
		

	context={'form':form}

	
	return render(request,'crime/register.html',context)


def login(request):
	if request.method == "POST":
		request.POST.get('username')
		request.POST.get('password')
		user=authenticate(request,username='username',password='password') 
		if user is not None:
			login(request,'user')
			return redirect('homepage')
		else:
			messages.info(request,'username or password is incorrect ')

	context={}
	return render(request,'crime/login.html',context) 
def logout(request):
	logout(request)
	return redirect('login')
	  	 

def registercrime(request):
	if request.method=="POST":
		Location=request.POST.get("Location")
		Nearest_police_post=request.POST.get("Nearest_police_post")
		summary_of_crime=request.POST.get("summary_of_crime")
		evidence=request.POST.get("evidence")

		new_crime= register_crime(Location='Location',Nearest_police_post='Nearest_police_post',summary_of_crime='summary_of_crime',evidence='evidence')
		new_crime.save()
	return render(request,'crime/registercrime.html')    

