from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from login.forms import SignUpForm, LoginForm
from login.models import SignUp

def home(request):
	if 'UserName' in request.session:
		UserName=request.session.get("UserName")
		print(UserName+"homeview()")
		return render(request,"login/index.html",{'UserName':UserName})		
	else:
		return render(request,"login/index.html")

def login(request):
	# form=LoginForm()
	if 'UserName' in request.session:
		return render(request,'login/login.html',{'UserName':request.session.get("UserName")})
	else:
		if request.method=="POST":
			form=LoginForm(data=request.POST)
			if form.is_valid():
				if SignUp.objects.filter(UserName=request.POST.get('UserName')).exists():
					profile=SignUp.objects.get(UserName=request.POST.get('UserName'))
					if profile.Password==request.POST.get('Password'):
						request.session['UserName']=profile.UserName
						return redirect("/")
					else:
						return render(request,'login/login.html',{'form':form,'msg':"Incorrect Password"})
				else:
					return render(request,'login/login.html',{'form':form,'msg':"User does not exists."})
		else:
			form=LoginForm()
		return render(request,'login/login.html',{'form':form})

def signup(request):
	if 'UserName' in request.session:
		return redirect("/")
	else:
		form=SignUpForm()
		if request.method=="POST":
			form=SignUpForm(request.POST)
			password=request.POST.get("Password")
			confirmPassword=request.POST.get("ConfirmPassword")
			if password==confirmPassword:
				if form.is_valid():
					form.save(commit=True)
					return redirect("login")
			else:
				return render(request,'login/signup.html',{'form': form,'msg':"Passwords does not match"})		
		return render(request,'login/signup.html',{'form': form})

def logout(request):
	if 'UserName' in request.session:
		del request.session['UserName']
		auth_logout(request)
	return redirect("/")