from django.contrib import admin
from .models import Symptom, Journal

# Register your models here.
admin.site.register(Symptom)
admin.site.register(Journal)
