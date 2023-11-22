import random
import tempfile
import os
from faker import Faker
from tracker.models import Symptom, Journal
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from django.core.files import File

fake = Faker()

def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username=username, email=email, password=password)
    return user

all_users = User.objects.all()

possible_areas = ["head", "neck", "back - upper",
                  "back - middle", "back - lower", "back - whole",
                  "shoulders - right", "shoulders - left", "shoulders - both",
                  "arms - right", "arms - left", "arms - both",
                  "hands - right", "hands - left", "hands - both",
                  "chest", "abdomen", "pelvis",
                  "legs - right", "legs - left", "legs - both",
                  "ankles - right", "ankles - left", "ankles - both",
                  "feet - left", "feet - right", "feet - both"
                ]

num_symptoms = 60

def get_random_image_file():
    image = Image.new('RGB', (200, 200), color=fake.color())
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), fake.word(), fill=fake.color())

    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        image.save(temp_file.name)
        return temp_file.name

# def seed_symptoms():
for _ in range(num_symptoms):
    user = random.choice(all_users) if all_users.exists() else create_user()
    area = fake.random_element(elements=possible_areas)
    severity = fake.random_int(min=1, max=10)
    triggers = fake.sentence()
    name = fake.word()
    notes = fake.paragraph()
    symptom_date = fake.date_this_decade()

    image_path = get_random_image_file()
    with open(image_path, 'rb') as image_file:
        image = File(image_file, name='random_image.png')

        Symptom.objects.create(
            user=user,
            area=area,
            severity=severity,
            triggers=triggers,
            name=name,
            notes=notes,
            image=image
        )

# os.remove(image_path)

print(f"Seeded {num_symptoms} symptoms successfully.")
