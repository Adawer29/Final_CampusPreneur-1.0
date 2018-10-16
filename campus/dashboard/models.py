from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
users=User.objects.all()


# Create your models here.
class Dashboard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Answer(models.Model):
    answer=models.TextField(blank=False,default='')
    name=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering= ["-name"]
