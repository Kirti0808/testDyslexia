from django import forms
from login.models import SignUp

class SignUpForm(forms.ModelForm):
    ConfirmPassword = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': "Re-enter the password"}))
    class Meta():
        model=SignUp
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'UserName': forms.TextInput(attrs={'placeholder': 'User name'}),            
            'Age': forms.TextInput(attrs={'placeholder': "Enter your age"}),
            'Password': forms.PasswordInput(attrs={'placeholder': "Give a strong password"}),
        }

class LoginForm(forms.Form):
    UserName = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    Password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder': "Give your password"}))