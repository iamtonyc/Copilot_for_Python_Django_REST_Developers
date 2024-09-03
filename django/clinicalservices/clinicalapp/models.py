from django.db import models

# Create your models here.


'''model class for patient data with autogenerate primary key id, first name, last name and age '''
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

'''model class for clinical data with autogenerate primary key id, component name, component value, 
measure date and patient id as foreign key to patient model'''
class ClinicalData(models.Model):
    id = models.AutoField(primary_key=True)
    component_name = models.CharField(max_length=100)
    component_value = models.CharField(max_length=100)
    measure_date = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

