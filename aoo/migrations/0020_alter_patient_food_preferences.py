# Generated by Django 3.2 on 2024-02-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0019_auto_20240221_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='food_preferences',
            field=models.ManyToManyField(blank=True, related_name='patients', to='aoo.FoodPreference'),
        ),
    ]
