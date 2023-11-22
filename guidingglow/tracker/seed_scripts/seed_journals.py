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


num_journals = 100

# def seed_journals():
for _ in range(num_journals):
    user = random.choice(all_users) if all_users.exists() else create_user()
    title = fake.sentence()
    body = fake.paragraphs(nb=3, ext_word_list=None)
    byline = fake.sentence()
    journal_date = fake.date_this_decade()

    image_path = get_random_image_file()
    with open(image_path, 'rb') as image_file:
        image = File(image_file, name='random_image.png')

        Journal.objects.create(
            author=user,
            title=title,
            body=body,
            image=image,
            byline=byline,
            date=journal_date
        )

# os.remove(image_path)

print(f"Seeded {num_journals} journal entries successfully.")
