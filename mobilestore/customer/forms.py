from django import forms
from .models import*


class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        exclude=["product","user"]
        widgets={
            "bank":forms.TextInput(attrs={"class":"form-control","placeholder":"Bank"}),
            "acholdername":forms.TextInput(attrs={"class":"form-control","placeholder":"AccountHolder"}),
            "accno":forms.TextInput(attrs={"class":"form-control","placeholder":"Account Number"}),
            "ifsc":forms.TextInput(attrs={"class":"form-control","placeholder":"IFSC Code"}),
            "quantity":forms.TextInput(attrs={"class":"form-control","placeholder":"Quantity"}),

        }