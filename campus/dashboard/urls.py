from django.urls import path,include
from . import views
from django.contrib import admin
app_name='dashboard'
urlpatterns=[
path('',views.Dashboardname.as_view(),name='dashboardname'),

]
