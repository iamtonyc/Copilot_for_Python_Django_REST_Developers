from rest_framework import serializers
from .models import Patient , ClinicalData


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalData
        fields = '__all__'
