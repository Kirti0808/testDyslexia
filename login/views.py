from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django import forms
import datetime, json
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import logout as auth_logout
from login.forms import SignUpForm, LoginForm, Test1Form
from login.models import SignUp, Test1Question, Test1, Test2

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
		return render(request,'login/login.html',{"UserName": request.session.get("UserName")})
	else:
		if request.method=="POST":
			form=LoginForm(data=request.POST)
			if form.is_valid():
				if SignUp.objects.filter(UserName=request.POST.get('UserName')).exists():
					profile=SignUp.objects.get(UserName=request.POST.get('UserName'))
					if profile.Password==request.POST.get('Password'):
						request.session['UserName']=profile.UserName
						# request.session['Test']=0
						return redirect("login")
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
				else:
					testUser=Test1()
					testUser.UserName=SignUp.objects.get(UserName=request.session.get("UserName"))
				testUser.score=sum
				testUser.save()
				# request.session['Test']=1
				return redirect("/test2")
		return render(request,'login/test1.html',{"UserName": request.session.get("UserName"),"form":form})
	else:
		return redirect("login")

def test2(request):
	if 'UserName' in request.session:
	# and request.session.get('Test')==1:
		if 'StartTime' not in request.session and 'EndTime' not in request.session:	
			return render(request,"login/test2.html")	
		elif 'StartTime' in request.session and 'EndTime' not in request.session:
			return render(request,"login/test2.html",{"startTime":"start"})
		else:
			request.session['EndTime']=json.loads(request.session.get('EndTime'))
			request.session['StartTime']=json.loads(request.session.get('StartTime'))
			if Test2.objects.filter(UserName=SignUp.objects.get(UserName=request.session.get("UserName"))).exists():
				testUser=Test2.objects.get(UserName=SignUp.objects.get(UserName=request.session.get("UserName")))
			else:
				testUser=Test2()
				testUser.UserName=SignUp.objects.get(UserName=request.session.get("UserName"))
			testUser.endTime=datetime.datetime.strptime(request.session['EndTime'], "%Y-%m-%dT%H:%M:%S.%f%z")
			print(testUser.endTime)
			print(request.session['EndTime'])
			testUser.startTime=datetime.datetime.strptime(request.session['StartTime'], "%Y-%m-%dT%H:%M:%S.%f%z")
			# Test2.calcTimediff(testUser)
			testUser.save()
			# request.session['Test']=2
			del request.session['StartTime']
			del request.session['EndTime']
			return redirect("test3")
	else:
		return redirect("login")
def test2Start(request):
	if 'UserName' in request.session:
		request.session['StartTime']=json.dumps(timezone.now(), cls=DjangoJSONEncoder)
		return redirect("test2")
	else:
		return redirect("login")
def test2Stop(request):
	if 'UserName' in request.session:
		print(datetime.datetime.now(timezone.utc))
		request.session['EndTime']=json.dumps(timezone.now(), cls=DjangoJSONEncoder)
		return redirect("test2")
	else:
		return redirect("login")

def test3(request):
	if 'UserName' in request.session:
		return render(request,"login/test3.html")
	else:
		return redirect("login")

def logout(request):
	if 'UserName' in request.session:
		del request.session['UserName']
		auth_logout(request)
	return redirect("/")