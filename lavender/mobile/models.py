from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
# Create your models here.


class Mobile(models.Model):
    brandName = models.CharField(max_length=50)
    modelName = models.CharField(max_length=500)
    color = models.CharField(max_length=150)
    janCode = models.DecimalField(unique=True, max_digits=13, decimal_places=0, validators=[MinValueValidator(8, message="JAN value is between 8 and 13 digit")])
    image = models.ImageField(upload_to='Mobile', null=True, blank=True, default='mobile.png')

    def __str__(self):
        return self.modelName

    def get_absolute_url(self):
        return reverse('Mobile List')
