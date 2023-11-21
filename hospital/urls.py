from django.urls import path
from .views import doctor_signup, signup_patient, create_appointment, doctor_appointment, patient_appointment

urlpatterns =[
    path('api/doctor/signup/', doctor_signup, name='doctor_signup'),
    path('api/patient/signup/', signup_patient, name='signup_patient'),
    path('api/appointment/create/', create_appointment, name='create_appointment'),
    path('api/doctor/appointment/', doctor_appointment, name='doctor_appointment'),
    path('api/patient/appointment/', patient_appointment, name='patient_appointment'),
]




