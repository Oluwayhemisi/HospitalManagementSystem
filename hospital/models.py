from django.db import models


# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=225)
    doctor_id = models.CharField(max_length=10, unique=True)

class Patient(models.Model):
    name = models.CharField(max_length=225)
    patient_id = models.CharField(max_length=10, unique=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField
