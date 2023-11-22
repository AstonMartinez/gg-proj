import random
import tempfile
from faker import Faker
from blog.models import BlogPost
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
from django.core.files import File

fake = Faker()

all_users = User.objects.all()

def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username=username, email=email, password=password)
    return user

def get_random_image_file():
    image = Image.new('RGB', (200, 200), color=fake.color())
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), fake.word(), fill=fake.color())

    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        image.save(temp_file.name)
        return temp_file.name

for _ in range(20):
    author_user = random.choice(all_users) if all_users.exists() else create_user()
    title = fake.sentence()
    body = fake.paragraphs(nb=3, ext_word_list=None)
    byline = fake.sentence()
    date = fake.date_this_decade()

    image_path = get_random_image_file()
    with open(image_path, 'rb') as image_file:
        image = File(image_file, name='random_image.png')

        BlogPost.objects.create(
            author=author_user,
            title=title,
            body=body,
            image=image,
            byline=byline,
            date=date
        )


print(f"Seeded 20 blog posts successfully.")
