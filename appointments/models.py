from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.get_full_name()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date} at {self.appointment_time}"
