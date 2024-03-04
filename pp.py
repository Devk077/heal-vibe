import os
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trial.settings')
import django
django.setup()

from aoo.models import Food, MealPlan, Patient, Appointments, MealPlanFood, BodyComposition
fake = Faker()

# Define function to generate random data for each model
def create_food():
    return Food.objects.create(
        name=fake.word(),
        calories=random.randint(50, 500),
        protein=random.randint(1, 50),
        carbs=random.randint(1, 100),
        fat=random.randint(1, 50)
    )

def create_meal_plan():
    return MealPlan.objects.create(
        name=fake.word(),
        short_description=fake.text()
    )

def create_patient():
    return Patient.objects.create(
        name=fake.name(),
        age=random.randint(18, 80),
        gender=random.choice(['Male', 'Female', 'Other']),
        height=random.uniform(150, 200),
        weight=random.uniform(50, 100)
    )

def create_body_composition(patient, patient_name):
    return BodyComposition.objects.create(
        Patient_name=patient_name,
        BMI=random.uniform(15, 40),
        weight=patient.weight,
        height=patient.height,
        body_fat=random.uniform(5, 30),
        age=patient.age,
        RMR=random.uniform(1200, 2500),
        visceral_fat=random.randint(1, 20)
    )

def create_appointment(patient, meal_plan):
    date_assigned = fake.date_time()
    date_assigned = timezone.make_aware(date_assigned, timezone.get_default_timezone())
    appointment = Appointments.objects.create(
        patient=patient,
        meal_plan=meal_plan,
        date_assigned=date_assigned,
        status=random.choice(['scheduled', 'confirmed', 'cancelled']),
        Appointment_description=fake.text()
    )
    create_body_composition(patient, patient.name)
    return appointment

def create_meal_plan_food(meal_plan, food):
    return MealPlanFood.objects.create(
        meal_plan=meal_plan,
        food=food,
        quantity=random.randint(1, 5),
        timing=random.choice(['breakfast', 'lunch', 'dinner', 'snacks', 'pre_workout', 'post_workout'])
    )

def populate(n):
    for _ in range(n):
        # Create sample food
        food = create_food()

        # Create sample meal plan
        meal_plan = create_meal_plan()

        # Create sample patient
        patient = create_patient()

        # Create sample appointment
        create_appointment(patient, meal_plan)

        # Create sample meal plan food
        create_meal_plan_food(meal_plan, food)

if __name__ == '__main__':
    # Define the number of instances to create
    num_instances = 15

    # Populate the database
    populate(num_instances)
