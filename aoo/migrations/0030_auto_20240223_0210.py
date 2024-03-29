# Generated by Django 3.2 on 2024-02-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0029_auto_20240221_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplanfood',
            name='time',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='irregular_period_details',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='regular_periods',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
