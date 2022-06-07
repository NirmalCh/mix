from calendar import c
from pickle import TRUE
from time import timezone
from typing import cast
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account_info(models.Model):
    # breakpoint()
    account_number= models.IntegerField(null=TRUE)
    citizenship_no = models.IntegerField(null=TRUE , blank=TRUE)
    images_fields = models.ImageField(null=TRUE ,upload_to='images/')
    address = models.CharField(max_length=100, null=TRUE)
    phone= models.IntegerField(null=TRUE)
    dob= models.DateField(null=TRUE , blank=TRUE)
    balance = models.IntegerField(null=TRUE)
    pdf=models.FileField(upload_to='static/media',default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.user}'
    


class City(models.Model):
    account_number= models.TextField(null=TRUE)
    account_info = models.OneToOneField(Account_info, on_delete=models.CASCADE)
 
    def __str__(self):
        return f'{self.account_number}'