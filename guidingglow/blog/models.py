from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True)
    byline = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, editable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'body': self.body,
            'byline': self.byline,
            'image': self.image,
            'date': self.date

        }

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'comment_author': self.comment_author,
            'body': self.body,
            'date_created': self.date_created,
            'date_updated': self.date_updated,
            'is_edited': self.is_edited
        }

class Like(models.Model):
    user_giving = models.ForeignKey(User, related_name='likes_given', on_delete=models.CASCADE)
    user_receiving = models.ForeignKey(User, related_name='likes_received', on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, related_name='likes', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_giving': self.user_giving,
            'user_receiving': self.user_receiving,
            'post': self.post,
            'date': self.date
        }
