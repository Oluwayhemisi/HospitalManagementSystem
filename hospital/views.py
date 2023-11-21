from django.shortcuts import render

from .models import Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def doctor_signup(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message':'Doctor signed up successfully'})
    return JsonResponse({'error':serializer.errors},status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signup_patient(request):
    if request.user.is_doctor:
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Patient signed up successfully'})
        return JsonResponse({'error': serializer.errors},status=400)
    return JsonResponse({'error':'Unauthorized'}, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message':'Appointment created successfully'})
    return JsonResponse({'error':serializer.errors},status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_appointment(request):
    doctor_appointments = Appointment.objects.filter(doctor=request.user.doctor)
    serializer = AppointmentSerializer(doctor_appointments,many=True)
    return JsonResponse({'appointments': serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_appointment(request):
    patient_appointments = Appointment.objects.filter(patient=request.user.patient)
    serializer = AppointmentSerializer(patient_appointments, many=True)
    return JsonResponse({'appointments':serializer.data})

