# Generated by Django 3.2 on 2024-02-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0025_remove_patient_water_glasses'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='water_glasses',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Glasses of water'),
        ),
        migrations.AddField(
            model_name='patient',
            name='water_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Water Quantity (L)'),
        ),
    ]
