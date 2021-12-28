from django import forms
from .models import *


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
