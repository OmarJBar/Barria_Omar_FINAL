# serializers.py

from rest_framework import serializers
from barria_mobile_app import models

class InscritoSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Inscrito
        fields = '__all__'