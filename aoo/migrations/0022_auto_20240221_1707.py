# Generated by Django 3.2 on 2024-02-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0021_auto_20240221_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='food_preferences',
        ),
        migrations.AddField(
            model_name='patient',
            name='food_preferences',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='FoodPreference',
        ),
    ]
