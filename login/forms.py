from django import forms
from login.models import SignUp, Test1, Test1Question

class SignUpForm(forms.ModelForm):
    ConfirmPassword = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': "Re-enter the password",'size':'40'}))
    class Meta():
        model=SignUp
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Full name','size':'40'}),
            'UserName': forms.TextInput(attrs={'placeholder': 'User name','size':'40'}),
            'Class': forms.TextInput(attrs={'placeholder': 'You present standard','size':'40'}),
            'Section': forms.TextInput(attrs={'placeholder': 'Section of your class','size':'40'}),
            'Gender': forms.TextInput(attrs={'placeholder': 'Male or Female','size':'40'}),            
            'Age': forms.TextInput(attrs={'placeholder': "Enter your age",'size':'40'}),
            'Phone': forms.TextInput(attrs={'placeholder': 'Give your phone number(10 digits)','size':'40'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Give an email','size':'40'}),
            'Percentage': forms.TextInput(attrs={'placeholder': 'Percentage obtained in your last exam','size':'40'}),
            'Password': forms.PasswordInput(attrs={'placeholder': "Give a strong password",'size':'40'}),
        }

class LoginForm(forms.Form):
    UserName = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User name','size':'40'}))
    Password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': "Give your password",'size':'40'}))

class Test1Form(forms.Form):
#     q=Test1Question.objects.get(id=1)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q1 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=2)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q2 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=3)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q3 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=4)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q4 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=5)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q5 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=6)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q6 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=7)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q7 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=8)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q8 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=9)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q9 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=10)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q10 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=11)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q11 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=12)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q12 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=13)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q13 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

#     q=Test1Question.objects.get(id=14)
#     CHOICES=[(q.yes,"Yes"), (q.no,"No"), (q.notSure,"Not Sure")]
#     q14 = forms.ChoiceField(label=q.Question,choices=CHOICES, widget=forms.RadioSelect())

    # class Meta():
    #     model=Test1
    #     fields= '__all__'