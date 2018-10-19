from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.db.models.signals import post_save
User=get_user_model()
users=User.objects.all()


# Create your models here.
class UserLoggedIn(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)
    class Meta:
        unique_together=('user','score')

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserLoggedIn.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)
