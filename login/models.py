from django.db import models

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
    Phone = models.IntegerField(null=False)
    Percentage = models.IntegerField(null=False)
    Password = models.CharField(max_length=264,null=False)

    def __str__(self):
        return self.UserName

# class Test1(models.Model):


