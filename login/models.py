from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class SignUp(models.Model):
    # UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=264,null=False)
    UserName = models.CharField(max_length=264,primary_key=True)
    Class = models.CharField(max_length=10,null=False)
    Section = models.CharField(max_length=1,null=False)
    Gender = models.CharField(max_length=10,null=False)
    Age = models.IntegerField(null=False)
    Email = models.EmailField(null=False)
    # Phone = models.IntegerField(null=False)
    Percentage = models.IntegerField(null=False)
    Password = models.CharField(max_length=264,null=False)

    def __str__(self):
        return self.UserName

class Test1Question(models.Model):
    Question = models.CharField(max_length=512, null=False)
    yes = models.IntegerField(null=False)
    no = models.IntegerField(null=False)
    notSure = models.IntegerField(null=False)

    def __str__(self):
        return self.Question

class Test1(models.Model):
    UserName = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True,null=True)  

    def __str__(self):
        return self.UserName.UserName

class Test2(models.Model):
    UserName = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    # startTime = models.DateTimeField(default=timezone.now,db_index=True)  
    # endTime = models.DateTimeField(default=timezone.now,db_index=True)  
    timeReq = models.DurationField(blank=True,null=True,db_index=True) 

    # def calcTimediff(self):
    #     self.timeReq = self.endTime-self.startTime
    #     return self

    def __str__(self):
        return self.UserName.UserName