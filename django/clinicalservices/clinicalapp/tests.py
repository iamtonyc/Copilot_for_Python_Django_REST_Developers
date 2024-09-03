from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSetTests(APITestCase):

    def setUp(self):
        self.patient_data = {'first_name':'John', 'last_name':'Doe', 'age': 30}
        self.patient = Patient.objects.create(**self.patient_data)
        self.url = reverse('patient-list')

    def test_create_patient(self):
        data = {'first_name':'Jane Doe', 'last_name':'king', 'age': 28}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 2)
        self.assertEqual(Patient.objects.get(id=response.data['id']).first_name, 'Jane Doe')

    def test_read_patient(self):
        response = self.client.get(self.url)
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_patient(self):
        data = {'first_name':'King', 'last_name':'Doe', 'age': 30}
        response = self.client.put(reverse('patient-detail', args=[self.patient.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.patient.refresh_from_db()
        self.assertEqual(self.patient.first_name, 'King')

    def test_delete_patient(self):
        response = self.client.delete(reverse('patient-detail', args=[self.patient.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)

    def test_get_all_patients(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import ClinicalData, Patient
from .serializers import ClinicalSerializer

class ClinicalViewSetTests(APITestCase):

    def setUp(self):
        # Create a Patient instance
        self.patient = Patient.objects.create(first_name='John', last_name='Doe', age=30)
        
        # Create ClinicalData instance
        self.clinical_data = {'component_name': 'AB', 'component_value': '10', 'patient': self.patient}
        self.clinical = ClinicalData.objects.create(**self.clinical_data)
        self.url = reverse('clinicaldata-list')

    def test_create_clinical(self):
        data = {'component_name': 'CD', 'component_value': '20', 'patient': self.patient.id}
        response = self.client.post(self.url, data, format='json')
        print(response.content)  # Print the response content for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClinicalData.objects.count(), 2)
        self.assertEqual(ClinicalData.objects.get(id=response.data['id']).component_name, 'CD')

    def test_read_clinical(self):
        response = self.client.get(self.url)
        clinicals = ClinicalData.objects.all()
        serializer = ClinicalSerializer(clinicals, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_clinical(self):
        data = {'component_name': 'EF', 'component_value': '15', 'patient': self.patient.id}
        print("self.clinical.id:" + str(self.clinical.id))
        response = self.client.put(reverse('clinicaldata-detail', args=[self.clinical.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clinical.refresh_from_db()
        self.assertEqual(self.clinical.component_name, 'EF')

    def test_delete_clinical(self):
        response = self.client.delete(reverse('clinicaldata-detail', args=[self.clinical.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ClinicalData.objects.count(), 0)