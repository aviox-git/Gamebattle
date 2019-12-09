from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages




# Create your views here.
def base(request):
	page = "homepage"
	return render(request,'dashboard/home.html',locals())

def layout(request):
	return render(request,'dashboard/layout.html')

def login(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get("password")
		if password and username:
			user = authenticate(username = username, password = password)
			if user is not None:
				auth_login(request,user)
				messages.success(request,'You are successfully logged in ')
				return HttpResponseRedirect('/dashboard')
			else:
				messages.error(request,'Invalid credential')
				return HttpResponseRedirect('/dashboard/login')
		return render(request,'login.html')


	return render(request,'dashboard/login.html')

def logouts(request):
	logout(request)
	messages.success(request,'you are successfully logged ')
	return HttpResponseRedirect('/dashboard/login')