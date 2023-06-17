from django import forms
from .models import Patient_Records
from .models import Appointment_Schedule

class Search_Form(forms.Form):
    last_name = forms.CharField(label='Last Name', max_length=100)
    first_name = forms.CharField(label='First Name', max_length=100)

class Patient_Records_Form(forms.ModelForm):
    class Meta:
        model = Patient_Records
        fields = ["patient_id", "last_name", "first_name", "age", "sex", "contact_number", "email"]

class Patient_Records_Form_Update(forms.ModelForm):
    class Meta:
        model = Patient_Records
        fields = ["age", "contact_number", "email"]


class Appointment_Schedule_Form(forms.ModelForm):
    class Meta:
        model = Appointment_Schedule
        fields = ["appointment_id", "patient_id", "last_appointment", "current_appointment_schedule", "appointment_time", "procedure", "status"]
        widgets = { 
            'last_appointment_schedule': forms.DateInput(attrs={'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_id'].widget.attrs['onchange'] = 'fetchLatestAppointmentSchedule()'
        self.fields['last_appointment'].required = False

class Appointment_Schedule_Form_Update(forms.ModelForm):
    class Meta:
        model = Appointment_Schedule
        fields = ["appointment_time", "status"]