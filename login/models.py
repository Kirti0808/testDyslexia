from django.db import models

# Create your models here.

class SignUp(models.Model):
    # UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=264,null=False)
    UserName = models.CharField(max_length=264,primary_key=True)
    Age = models.IntegerField(null=False)
    Password = models.CharField(max_length=264,null=False)

    def __str__(self):
        return self.UserName

