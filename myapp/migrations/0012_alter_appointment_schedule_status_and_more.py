# Generated by Django 4.2.1 on 2023-06-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_appointment_schedule_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_schedule',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Missed', 'Missed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='patient_records',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]