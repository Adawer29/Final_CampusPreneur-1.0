from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from django.core.files.storage import FileSystemStorage
User=get_user_model()
# Create your models here.
from django import template
register=template.Library()
class Answer(models.Model):
    name=models.CharField(max_length=10,unique=True)
    answer=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering= ["-name"]

class Question(models.Model):
    question_relation=models.ForeignKey(Answer,related_name='ques',on_delete=models.CASCADE)
    question_image=models.ImageField(upload_to='levels/')
    text=models.TextField(blank=True,max_length=100)

    def __str__(self):
        return str(self.question_relation)
