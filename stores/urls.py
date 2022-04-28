from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('category/',views.category,name='category'),
    path('singleproduct/<slug:slug>/',views.singleproduct,name='singleproduct'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('myCart/',views.myCart,name='myCart'),
    path('manageCart/<int:id>/',views.manageCart,name='manageCart'),
    path('emptyCart/',views.emptyCart,name='emptyCart'), 
    path('checkout/',views.checkout,name='checkout'),
    path('register/',views.register,name='register'),
    path('loginuser/',views.loginuser,name='login'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('profile/',views.profile,name='profile'),
    path('order-detail/<int:id>/',views.orderDetails,name='order-detail'),
    path('search/',views.search,name='search'),
    path('transfer/',views.transferPage,name='transfer'),
    path('payment/<int:id>/',views.paymentPage,name='payment'),
    path('<str:ref>/',views.verify_payment,name='verify-payment'),




]