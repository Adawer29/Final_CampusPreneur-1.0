from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name='levels'
urlpatterns =[
path('arena1/',views.Arena1,name='level1')]
