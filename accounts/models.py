from django.db import models
from django.contrib.auth.models import AbstractUser

#  Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=10) 


class owner(models.Model):
    reg_no=models.CharField(max_length=25)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    



class Turffdetails(models.Model):
    turff_name=models.CharField(max_length=30)
    turff_address=models.TextField()
    turff_img=models.ImageField(null=True,blank=True)
    contact=models.CharField(max_length=12)
    court_fee=models.CharField(max_length=100)
    court_size=models.CharField(max_length=50)
    t_email=models.EmailField(max_length=50)
    turff_owner=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    def __str__(self) -> str:
        return self.turff_name
    
class Tbooking(models.Model):
    c_name=models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    detail=models.ForeignKey(
        to=Turffdetails,
        on_delete=models.CASCADE
    )
    date=models.DateField()
    s_time=models.TimeField()
    e_time=models.TimeField()
    amount=models.BigIntegerField(default=0)
    duration=models.FloatField(default=0.0)
