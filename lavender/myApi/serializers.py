from rest_framework import serializers
from mobile.models import *


class mobileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
