from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CensorInfo(models.Model):
    rating=models.CharField(max_length=10)
    certified_by = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.rating




class Director(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Movieinfo(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    description=models.TextField(blank=True,null=True)
    poster=models.ImageField(upload_to='images/',blank=True,null=True)
    censor_details = models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies',null=True) 
    
    directed_by = models.ForeignKey(Director,null=True,on_delete=models.CASCADE,related_name="directed_movies")
    def __str__(self):
        return self.title






