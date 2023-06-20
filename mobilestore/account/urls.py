from django.urls import path
from .views import *
urlpatterns=[
    path('reg/',Reg.as_view(),name="reg"),
    path('logout/',LogOut.as_view(),name="lo"),
]