# Generated by Django 4.2.1 on 2023-06-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_appointment_schedule_last_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_schedule',
            name='last_appointment',
            field=models.DateField(default=models.DateField(), null=True),
        ),
    ]