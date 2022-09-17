from django.db import models

# Create your models here.

class patient_details(models.Model):
    patient_name=models.CharField(max_length=255)
    age=models.TextField()
    gender=models.TextField()
    email=models.EmailField()
    phone_number=models.TextField()
    department=models.TextField()
    date=models.TextField()
   
