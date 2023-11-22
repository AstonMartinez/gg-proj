import random
from faker import Faker
from blog.models import BlogPost, Like
from django.contrib.auth.models import User

fake = Faker()

def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username=username, email=email, password=password)
    return user

all_users = User.objects.all()
all_blog_posts = BlogPost.objects.all()

num_likes = 100

# def seed_likes():
for _ in range(num_likes):
    user_giving = random.choice(all_users) if all_users.exists() else create_user()
    user_receiving = random.choice(all_users.exclude(pk=user_giving.pk)) if all_users.exists() else create_user()
    blog_post = random.choice(all_blog_posts) if all_blog_posts.exists() else None
    like_date = fake.date_this_decade()

    Like.objects.create(
        user_giving=user_giving,
        user_receiving=user_receiving,
        post=blog_post,
        date=like_date
    )

print(f"Seeded {num_likes} likes successfully.")
