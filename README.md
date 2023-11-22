# HospitalManagementSystem


#getting started

pip install Django

activate virtual enviroment

django-admin startproject hospitalmanagementsystem

cd hospitalmanagementsystem

pip install djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

#usage
To sign up a new doctor, send a POST request to /api/doctor/signup/

To sign up a new patient, send a POST request to /api/patient/signup/

To create a new appointment, send a POST request to /api/appointment/create/

View Doctor Appointments
To view all appointments for a doctor, send a GET request to /api/doctor/appointment/.

View Patient Appointments
To view all appointments for a patient, send a GET request to /api/patient/appointment/


