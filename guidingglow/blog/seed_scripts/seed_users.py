from faker import Faker
from django.contrib.auth.models import User

fake = Faker()


def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username=username, email=email, password=password)
    return user

num_users = 10

# def seed_users():
User.objects.create_user(username='DemoLition', email='demo@aa.io', password='password')
for _ in range(num_users):
    username = fake.user_name()
    email = fake.email()
    password = 'password'

    user = User.objects.create_user(username=username, email=email, password=password)

    user.first_name = fake.first_name()
    user.last_name = fake.last_name()
    user.save()

print(f"Seeded {num_users} users successfully.")
