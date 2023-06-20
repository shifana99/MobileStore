from django.urls import path
from .views import *
urlpatterns=[
    path('home/',StoreHome.as_view(),name="sh"),
    path('ap/',AddProduct.as_view(),name="ap"),
    path('mp/',MyProduct.as_view(),name="mp"),
    path('cp/',ChangePassword.as_view(),name="cp"),
    path('dp/<int:pk>/',DeleteProduct.as_view(),name="dp"),
    path('ep/<int:pk>/',EditProduct.as_view(),name="ep"),
]