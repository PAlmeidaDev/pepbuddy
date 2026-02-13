from django.shortcuts import render

from rest_framework import viewsets
from .models import Medication
from .serializers import MedicationSerializer


class MedicationViewSet(viewsets.ModelViewSet):
    # Tell the view which data to get
    queryset = Medication.objects.all()

    # Tell the view which translator to use
    serializer_class = MedicationSerializer

    # Logic: Only show the medications belonging to the logged-in user
    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
