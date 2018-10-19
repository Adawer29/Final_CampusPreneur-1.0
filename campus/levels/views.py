from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import *
from . import models
from django import forms
from .forms import CheckAnswer
from django.contrib.auth.decorators import login_required
from .models import Question
from dashboard.models import UserLoggedIn

# Create your views here.
@login_required
def Arena1(request):
    data=UserLoggedIn.objects.all()
    if request.method=='POST':
        form = CheckAnswer(request.POST)
        if form.is_valid():
            return redirect('thanks')
    else:
        form=CheckAnswer()
    args={'form':form,'data':data}
    return render(request,'levels/arena1.html',args)
