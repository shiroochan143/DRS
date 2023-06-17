from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

status_choices = [("Pending", "pending"), ("Done", "done"), ("Missed", "missed")]
sex_choices = [("Male", "male"), ("Female", "female")]

class Patient_Records(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10, choices=sex_choices)
    contact_number = models.CharField(max_length=12)    
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.patient_id} : {self.last_name}"
    


class Appointment_Schedule(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_Records, on_delete=models.CASCADE)
    current_appointment_schedule = models.DateField()
    last_appointment = models.DateField(default=None, null=True)
    appointment_time = models.TimeField()
    procedure = models.CharField(max_length=100)
    status = models.CharField(max_length=30, choices=status_choices)

    def __str__(self):
        return f"{self.status}"


    def save(self, *args, **kwargs):
        if self.appointment_time is not None:
            self.appointment_time = self.appointment_time.replace(microsecond=0)
        super().save(*args, **kwargs)