import random
from faker import Faker
from blog.models import BlogPost, Comment
from django.contrib.auth.models import User

fake = Faker()

def create_user():
    username = fake.user_name()
    email = fake.email()
    password = fake.password()

    user = User.objects.create_user(username=username, email=email, password=password)
    return user

all_blog_posts = BlogPost.objects.all()
all_users = User.objects.all()

num_comments = 50

# def seed_comments():
for _ in range(num_comments):
    comment_author = random.choice(all_users) if all_users.exists() else create_user()
    comment_body = fake.paragraph()
    comment_date = fake.date_this_decade()
    is_edited = fake.boolean()

    blog_post = random.choice(all_blog_posts) if all_blog_posts.exists() else None

    Comment.objects.create(
        post=blog_post,
        comment_author=comment_author,
        body=comment_body,
        date_created=comment_date,
        date_updated=comment_date,
        is_edited=is_edited
    )

print(f"Seeded {num_comments} comments successfully.")
