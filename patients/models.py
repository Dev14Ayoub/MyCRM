from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()
