# Generated by Django 3.2 on 2024-02-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0018_alter_patient_food_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('VEG', 'Veg'), ('NON VEG', 'Non-Veg'), ('EGG', 'Egg'), ('CHICKEN', 'Chicken'), ('SEA FOOD', 'Sea-Food')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='food_preference',
        ),
        migrations.AddField(
            model_name='patient',
            name='food_preferences',
            field=models.ManyToManyField(blank=True, null=True, related_name='patients', to='aoo.FoodPreference'),
        ),
    ]
