from django.db import models

# Create your models here.
from django import forms
from captcha.fields import CaptchaField

class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()
    
