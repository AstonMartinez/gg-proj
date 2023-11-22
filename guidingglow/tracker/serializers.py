from rest_framework import serializers
from .models import Symptom, Journal

class SymptomSerializer(serializers.Models):
    class Meta:
        model = Symptom
        fields = '__all__'

class JournalSerializer(serializers.Models):
    class Meta:
        model = Journal
        fields = '__all__'
