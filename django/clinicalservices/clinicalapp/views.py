from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient , ClinicalData
from .serializers import PatientSerializer , ClinicalSerializer


# Create your views here.
#viewset for patient that uses the patient serializer   
class PatientViewSet(viewsets.ModelViewSet):            
    queryset = Patient.objects.all()        
    serializer_class = PatientSerializer


#viewset for clinical that uses the clincial data serializer       
class ClinicalDataViewSet(viewsets.ModelViewSet):            
    queryset = ClinicalData.objects.all()        
    serializer_class = ClinicalSerializer
    
