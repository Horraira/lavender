from django import forms
from .models import *


class Mobile(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
