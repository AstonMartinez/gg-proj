from rest_framework import generics, permissions
from .models import Symptom, Journal
from .serializers import SymptomSerializer, JournalSerializer

class SymptomListView(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Symptom.objects.filter(user=self.request.user)

class SymptomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [permissions.IsAuthenticated]

class SymptomCreateView(generics.CreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SymptomUpdateView(generics.UpdateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Symptom.objects.filter(user=self.request.user)

class SymptomDeleteView(generics.DestroyAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Symptom.objects.filter(user=self.request.user)

class JournalListView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(author=self.request.user)

class JournalCreateView(generics.CreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class JournalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

class JournalUpdateView(generics.UpdateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(author=self.request.user)

class JournalDeleteView(generics.DestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(author=self.request.user)
