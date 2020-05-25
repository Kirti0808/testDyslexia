from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from login.forms import SignUpForm, LoginForm, Test1Form
from login.models import SignUp, Test1Question, Test1

def home(request):
	if 'UserName' in request.session:
		UserName=request.session.get("UserName")
		print(UserName+"homeview()")
		return render(request,"login/index.html",{'UserName':UserName})		
	else:
		return render(request,"login/index.html")

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

def login(request):
	# form=LoginForm()
	if 'UserName' in request.session:
		return render(request,'login/afterlogin.html',{"UserName": request.session.get("UserName")})
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

def test1(request):
	if 'UserName' in request.session:
		form=Test1Form
		if request.method=="POST":
			form=Test1Form(data=request.POST)
			if form.is_valid():
				sum=0
				for f in range (1,15):
					field="q"+str(f)
					sum=sum+int(request.POST.get(field))
				# print(sum)
				if Test1.objects.filter(UserName=SignUp.objects.get(UserName=request.session.get("UserName"))).exists():
					testUser=Test1.objects.get(UserName=SignUp.objects.get(UserName=request.session.get("UserName")))
					testUser.score=sum
				else:
					testUser=Test1()
					testUser.UserName=SignUp.objects.get(UserName=request.session.get("UserName"))
					testUser.score=sum
				testUser.save()
				return redirect("/")
		return render(request,'login/test1.html',{"UserName": request.session.get("UserName"),"form":form})
	else:
		return redirect("login")

def logout(request):
	if 'UserName' in request.session:
		del request.session['UserName']
		auth_logout(request)
	return redirect("/")