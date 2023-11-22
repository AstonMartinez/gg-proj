from django.urls import path
from .views import (
    SymptomListView, SymptomDetailView, JournalListView, JournalDetailView,
    SymptomCreateView, SymptomUpdateView, SymptomDeleteView, JournalCreateView,
    JournalUpdateView, JournalDeleteView

    )

urlpatterns = [
    path('symptoms/all', SymptomListView.as_view(), name='symptoms-list'),
    path('symptoms/<int:pk>', SymptomDetailView.as_view(), name='symptom-details'),
    path('journals/all', JournalListView.as_view(), name='journal-list'),
    path('journals/<int:pk>', JournalDetailView.as_view(), name='journal-detail'),
    path('symptoms/new/', SymptomCreateView.as_view(), name='symptom-create'),
    path('symptoms/<int:pk>/update/', SymptomUpdateView.as_view(), name='symptom-update'),
    path('symptoms/<int:pk>/delete/', SymptomDeleteView.as_view(), name='symptom-delete'),
    path('journals/new/', JournalCreateView.as_view(), name='journal-create'),
    path('journals/<int:pk>/update/', JournalUpdateView.as_view(), name='journal-update'),
    path('journals/<int:pk>/delete/', JournalDeleteView.as_view(), name='journal-delete'),
]
