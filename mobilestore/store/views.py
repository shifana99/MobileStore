from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,View,UpdateView,DeleteView,FormView
from django.contrib.auth import authenticate,logout
from account.models import CustomerUser
from account.forms import*
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import*
from .models import*



# Create your views here.

class StoreHome(TemplateView):
    template_name="storehome.html"

class AddProduct(CreateView):
    form_class=ProductForm
    model=Product
    template_name="addproduct.html"
    success_url=reverse_lazy("sh")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MyProduct(TemplateView):
    template_name="myproduct.html"   
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs) 
        context["data"]=Product.objects.filter(user=self.request.user)
        return context
    

class DeleteProduct(DeleteView):
    model=Product
    template_name="deleteproduct.html"
    success_url=reverse_lazy('mp')
    pk_url_kwarg="pk"   
  

class EditProduct(UpdateView):
    form_class=ProductForm
    model=Product
    template_name="editproduct.html"
    success_url=reverse_lazy('mp')
    pk_url_kwargs="pk"   


class ChangePassword(FormView):
        template_name="changepassword.html"
        form_class=ChangePasswordForm
        def post(self,request,*args,**kwrgs):
             form_data=ChangePasswordForm(data=request.POST)
             if form_data.is_valid():
                  current=form_data.cleaned_data.get("current_password")
                  new=form_data.cleaned_data.get("new_password")
                  confirm=form_data.cleaned_data.get("confirm_password")
                  print(current)
                  user=authenticate(request,username=request.user.username,password=current)
                  if user:
                    if new==confirm:
                            user.set_password(new)
                            user.save()
                            messages.success(request,"Password Changed!!!")
                            logout(request)
                            return redirect("log")
                    else:
                            messages.error(request,"Password Mismatches!!")
                            return redirect("cp")
                  else:
                       messages.error(request,"Incorrect Password!!!")
                       return redirect("cp")
             else:
                  return render(request,"change_password.html",{"form":form_data})    



