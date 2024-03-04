# Generated by Django 3.2 on 2024-02-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0013_auto_20240220_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplanfood',
            name='timing',
            field=models.CharField(choices=[('after_bed', 'After Bed'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('snacks', 'Snacks'), ('dinner', 'Dinner'), ('before_bed', 'Before Bed'), ('pre_workout', 'Pre-Workout'), ('post_workout', 'Post-Workout')], default='', max_length=20, verbose_name='Timing'),
        ),
    ]