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
    # qlist=Test1Question.objects.all()
    # for q in qlist:
    # q1=models.IntegerField(null=False)
    # q2=models.IntegerField(null=False)
    # q3=models.IntegerField(null=False)
    # q4=models.IntegerField(null=False)
    # q5=models.IntegerField(null=False)
    # q6=models.IntegerField(null=False)
    # q7=models.IntegerField(null=False)
    # q8=models.IntegerField(null=False)
    # q9=models.IntegerField(null=False)
    # q10=models.IntegerField(null=False)
    # q11=models.IntegerField(null=False)
    # q12=models.IntegerField(null=False)
    # q13=models.IntegerField(null=False)
    # q14=models.IntegerField(null=False)
    UserName = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    score = models.IntegerField(blank=True,null=True)  

    def __str__(self):
        return self.UserName.UserName