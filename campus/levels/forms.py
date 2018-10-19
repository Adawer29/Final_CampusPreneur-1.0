from django import forms
from .models import Answer
from django.core.exceptions import ObjectDoesNotExist
from . import views
class CheckAnswer(forms.Form):
    your_answer=forms.CharField(label='Answer')
    def clean(self):
        cleaned_data=super(CheckAnswer,self).clean()
        response=cleaned_data.get("your_answer")


        try:
            p = Answer.objects.get(answer__iexact=response)
        except Answer.DoesNotExist:
            raise forms.ValidationError("Wrong Answer.")
