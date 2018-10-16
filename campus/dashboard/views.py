from django.shortcuts import render
from .import models
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
class Dashboardname(TemplateView):
    model=models.Dashboard
    context_object_name='dashboard_user'
    template_name='dashboard/dashboard.html'
    
