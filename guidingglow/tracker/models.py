from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Symptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=255)
    severity = models.IntegerField()
    triggers = models.TextField()
    name = models.CharField(max_length=255)
    notes = models.TextField()
    date = models.DateField(auto_now_add=True, editable=True)
    image = models.ImageField(upload_to='symptom_images/', null=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'area': self.area,
            'severity': self.severity,
            'triggers': self.triggers,
            'name': self.name,
            'notes': self.notes,
            'date': self.date,
            'image': self.image
        }

class Journal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='journal_images/', null=True)
    byline = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, editable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'title': self.title,
            'body': self.body,
            'image': self.image,
            'byline': self.byline,
            'date': self.date
        }
