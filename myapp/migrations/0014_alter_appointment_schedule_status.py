# Generated by Django 4.2.1 on 2023-06-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_patient_records_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_schedule',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Missed', 'Missed')], max_length=15),
        ),
    ]
