from django import forms
from .models import*


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=["user"]
        widgets={
            "productname":forms.TextInput(attrs={"class":"form-control","placeholder":"productname"}),
            "image":forms.FileInput(),
            "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"price"}),
            "ram":forms.TextInput(attrs={"class":"form-control","placeholder":"ram"}),
            "rom":forms.TextInput(attrs={"class":"form-control","placeholder":"rom"}),
            "battery":forms.TextInput(attrs={"class":"form-control","placeholder":"battery"}),
            "processor":forms.TextInput(attrs={"class":"form-control","placeholder":"processor"}),

        }

class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=100,label="Current Password",widget=forms.PasswordInput)
    new_password=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput)

