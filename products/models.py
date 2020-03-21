from django.db import models
from django.contrib.auth.models import User
import string
from random import random, choice

class Product(models.Model):

    body=models.TextField(default='000000',editable=True)
    image=models.ImageField(upload_to='images/')
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    post_mode=models.CharField(max_length=20,default="0000")



    def summary(self):
        return self.hunter
