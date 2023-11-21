from django.test import TestCase
from .models import Doctor,Patient

# Create your tests here.

class HospitalManagementSystemTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(name='Dr Bala', doctor_id='DR123')
        self.patient = Patient.objects.create(name='Yemisi Ismail', patient_id ='P222')

    def test_doctor_signup(self):
        self.assertEqual(self.doctor.name, 'Dr Bala')
        self.assertEqual(self.doctor.doctor_id, 'DR123')
    def test_patient_signup(self):
        self.assertEqual(self.patient.name, 'Yemisi Ismail')
        self.assertEqual(self.patient.patient_id, 'P222')
