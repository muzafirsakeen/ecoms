from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib import admin
from mistershoppie import admin
from . import views





urlpatterns = [
    path('',views.user_login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('display/',views.display,name='display'),
    path('logout/',views.logout,name='logout')



]