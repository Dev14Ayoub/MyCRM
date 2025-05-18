from django import forms
from .models import Appointment

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'appointment_date', 'appointment_time', 'reason']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }
