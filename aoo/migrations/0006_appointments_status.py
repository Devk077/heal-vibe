# Generated by Django 3.2 on 2024-02-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0005_alter_appointments_meal_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='scheduled', max_length=20),
        ),
    ]
