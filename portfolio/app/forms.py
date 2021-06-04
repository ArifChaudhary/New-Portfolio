from django.core import validators
from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from django.utils.translation import gettext, gettext_lazy as _
from . models import User

class Registration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name', 'email', 'subject', 'message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
            }
        
