from django import forms
from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    class Meta:
        model=CustomerUser
        fields=["first_name","last_name","email","phone","address","usertype","username","password1","password2"]
        
        

class LogForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))  
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))             
