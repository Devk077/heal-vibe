# Generated by Django 3.2 on 2024-02-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0010_auto_20240220_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.PositiveIntegerField(verbose_name='Calories (Kcals)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.PositiveIntegerField(verbose_name='Carbohydrates (grams)'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.PositiveIntegerField(verbose_name='Fat(Kcal/g )'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.PositiveIntegerField(verbose_name='Protein (grams)'),
        ),
    ]
