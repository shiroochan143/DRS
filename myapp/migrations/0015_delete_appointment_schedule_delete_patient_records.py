# Generated by Django 4.2.1 on 2023-06-22 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_appointment_schedule_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment_Schedule',
        ),
        migrations.DeleteModel(
            name='Patient_Records',
        ),
    ]