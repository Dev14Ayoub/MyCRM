from django.db import models
from appointments.models import Appointment

class Invoice(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.appointment}"

