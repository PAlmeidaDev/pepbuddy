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

        # 1. Safety Check (Keep this!)
        if medication.current_stock <= 0:
            return Response(
                {'error': 'Out of stock! Cannot log dose.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2. The "Memory" (New Logic)
        # We create a record in the history table before updating the main record
        DoseLog.objects.create(medication=medication)

        # 3. The "Now" (Keep this!)
        medication.last_taken = timezone.now()
        medication.current_stock -= 1
        medication.save()

        return Response({
            'status': 'Dose logged successfully',
            'new_stock': medication.current_stock,
            'next_dose': medication.next_dose_time,
            # Optional: you could even return the log count
            'total_doses_taken': medication.logs.count()
        })