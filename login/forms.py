from django import forms
from login.models import SignUp

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
            'Phone': forms.TextInput(attrs={'placeholder': 'Give your phone number','size':'40'}),
            'Email': forms.EmailInput(attrs={'placeholder': 'Give an email','size':'40'}),
            'Percentage': forms.TextInput(attrs={'placeholder': 'Percentage obtained in your last exam','size':'40'}),
            'Password': forms.PasswordInput(attrs={'placeholder': "Give a strong password",'size':'40'}),
        }

class LoginForm(forms.Form):
    UserName = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User name','size':'40'}))
    Password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': "Give your password",'size':'40'}))