# Generated by Django 3.2 on 2024-02-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0026_auto_20240221_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='coffee_consumption',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='milk_consumption',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='tea_consumption',
        ),
        migrations.AddField(
            model_name='patient',
            name='beverages',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='Beverages'),
        ),
    ]
