# Generated by Django 3.2 on 2024-02-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0017_auto_20240221_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='food_preference',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg'), ('Egg', 'Egg'), ('Chicken', 'Chicken'), ('Sea-Food', 'Sea-Food')], default='', max_length=20),
        ),
    ]
