from django import forms

from .models import Patient_Records
from .models import Appointment_Schedule


class Search_Form(forms.Form):
    full_name = forms.CharField(label='Name')

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        first_name, last_name = map(str.strip, full_name.rsplit(" ", 1))
        # first_name = full_name.split(' ', 1) if ' ' in full_name else ('', '')
        self.cleaned_data['first_name'] = first_name
        self.cleaned_data['last_name'] = last_name
        return full_name
    
class Search_Date(forms.Form):
       date = forms.DateField(label='Search by Date')

class Patient_Records_Form(forms.ModelForm):
    class Meta:
        model = Patient_Records
        fields = ["patient_id", "last_name", "first_name", "age", "sex", "contact_number", "email"]
        widgets= {
            'last_name' : forms.TextInput(attrs={'placeholder' : 'Dela Cruz'}),
            'first_name' : forms.TextInput(attrs={'placeholder' : 'Juan'}),
            'age' : forms.NumberInput(attrs={'placeholder' : '18'}),
            'sex' : forms.TextInput(attrs={'placeholder' : 'Male or Female'}),
            'contact_number' : forms.TextInput(attrs={'placeholder' : '09573618842'}),
            'email' : forms.TextInput(attrs={'placeholder' : 'juan.delacruz@gmail.com'}),
        } 

class Patient_Records_Form_Update(forms.ModelForm):
    class Meta:
        model = Patient_Records
        fields = ["age", "contact_number", "email"]


class Appointment_Schedule_Form(forms.ModelForm):
    class Meta:
        model = Appointment_Schedule
        fields = ["appointment_id", "patient_id", "last_appointment", "current_appointment_schedule", "appointment_time", "procedure"]
        widgets = { 
            'last_appointment_schedule': forms.DateInput(attrs={'readonly': 'readonly', 'placeholder' : '2023-01-12'}),
            'current_appointment_schedule' : forms.DateInput(attrs={'placeholder' : '2023-05-15'}),
            'appointment_time' : forms.TimeInput(attrs= {'placeholder' : 'military time format - 7:15 or 15:30'}),
            'procedure' : forms.TextInput(attrs={'placeholder' : 'short description'})
        }

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('current_appointment_schedule')
        appointment_time1 = cleaned_data.get('appointment_time')

        if appointment_date and appointment_time1:
            existing_appointments = Appointment_Schedule.objects.filter(current_appointment_schedule=appointment_date, appointment_time=appointment_time1)
            if existing_appointments.exists():
                self.add_error('appointment_time', 'An appointment with this time already exists for the selected date.')
        
        return cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_id'].widget.attrs['onchange'] = 'fetchLatestAppointmentSchedule()'
        self.fields['last_appointment'].required = False

class Appointment_Schedule_Form_Update(forms.ModelForm):
    class Meta:
        model = Appointment_Schedule
        fields = ["appointment_time", "procedure", "status"]
        widgets = {
            'appointment_time' : forms.TimeInput(attrs={'placeholder' : 'military time format - 7:15 or 15:30'}),
            'procedure' : forms.TextInput(attrs={'placeholder' : 'short description'})
        }