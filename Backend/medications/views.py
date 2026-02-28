from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import viewsets
from .models import Medication, DoseLog
from .serializers import MedicationSerializer
from django.contrib.auth.models import User


class MedicationViewSet(viewsets.ModelViewSet):
    # Tell the view which data to get
    queryset = Medication.objects.all()

    # Tell the view which translator to use
    serializer_class = MedicationSerializer

    def perform_create(self, serializer):  # big safety risk only being used for testing will be removed after.
        if self.request.user.is_authenticated:
            # If logged in, use that user
            serializer.save(user=self.request.user, last_taken=timezone.now())
        else:
            # If not logged in (Anonymous), use the first user in the database (your admin)
            first_user = User.objects.first()
            serializer.save(user=first_user, last_taken=timezone.now())

    # Logic: Only show the medications belonging to the logged-in user
    def get_queryset(self):
        # Temporarily comment out the filter so React can see the data
        # return Medication.objects.filter(user=self.request.user)


        return Medication.objects.all()

    @action(detail=True, methods=['post'])
    def log_dose(self, request, pk=None):
        medication = self.get_object()

        # Check if user wants to "Shift" the schedule
        # Default to False if the frontend doesn't send it
        adjust_schedule = request.data.get('adjust_future_schedule', False)

        if medication.current_stock <= 0:
            return Response({'error': 'Out of stock!'}, status=400)

        # 1. Create the History Log
        DoseLog.objects.create(medication=medication)

        # 2. Logic for the "Next Dose"
        now = timezone.now()

        if adjust_schedule:
            # PATH A: The "Adjusted" Path
            # We set the last_taken to 'now', which shifts the whole schedule forward
            medication.last_taken = now
        else:
            # PATH B: The "Strict" Path
            # If it was due at 12:00 and you took it at 2:00, but want to stay on track:
            # We calculate where the last dose 'should' have been.
            # For now, setting it to 'now' is standard, but if we want to be strict,
            # we can calculate the previous 'expected' slot.
            # Simplest version: stay on the current timestamp logic.
            medication.last_taken = now

        medication.current_stock -= 1
        medication.save()

        return Response({'status': 'Dose logged'})