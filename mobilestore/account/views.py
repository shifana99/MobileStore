from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView,View
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import CustomerUser
from django.contrib.auth.models import User

# Create your views here.

# class MainHome(TemplateView):
#     template_name="mainhome.html"

class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=CustomerUser
    success_url=reverse_lazy("log")

class Log(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwrgs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            us=form_data.cleaned_data.get("username")    
            ps=form_data.cleaned_data.get("password") 
            user=authenticate(request,username=us,password=ps)
            if user:
                login(request,user)
                if request.user.usertype == "store":
                    return redirect("sh")
                else:
                    return redirect("uh")
            else:              
                return render(request,"login.html",{"form":form_data})  
        else:           
            return render(request,"login.html",{"form":form_data})      

class LogOut(View):
     def get(self,request):
        logout=(request)
        return redirect("log")            