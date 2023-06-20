from django.urls import path
from .views import *
urlpatterns=[
    path('home/',UserHome.as_view(),name="uh"),
    path('mp/',ProductView.as_view(),name="pv"),
    path('addtocart/<int:cid>',addtocart,name="ac"),
    path('cart/',CartView.as_view(),name="cart"),
    path('remove/<int:pk>/',RemoveCart.as_view(),name="rc"),
    path('buy/<int:pid>/',BuyView.as_view(),name="buy"),
    path('pay/<int:pid>/',PaymentConfirm,name="pay"),
    path('mo/',MyOrders.as_view(),name="mo"),
    path('cancel/<int:pk>/',CancelOrders.as_view(),name="co"),




]