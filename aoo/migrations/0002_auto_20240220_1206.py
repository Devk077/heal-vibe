# Generated by Django 3.2 on 2024-02-20 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aoo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.PositiveIntegerField()),
                ('protein', models.PositiveIntegerField()),
                ('carbs', models.PositiveIntegerField()),
                ('fat', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MealPlanFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('food', models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to='aoo.food')),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoo.mealplan')),
            ],
        ),
        migrations.RemoveField(
            model_name='dietitem',
            name='diet',
        ),
        migrations.RemoveField(
            model_name='dietitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='patientdiet',
            name='diet',
        ),
        migrations.RemoveField(
            model_name='patientdiet',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='diets',
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='other', max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Diet',
        ),
        migrations.DeleteModel(
            name='DietItem',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='PatientDiet',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='foods',
            field=models.ManyToManyField(through='aoo.MealPlanFood', to='aoo.Food'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='meal_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoo.mealplan'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoo.patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='meal_plans',
            field=models.ManyToManyField(through='aoo.Appointments', to='aoo.MealPlan'),
        ),
    ]
