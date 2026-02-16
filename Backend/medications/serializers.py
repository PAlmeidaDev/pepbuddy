from rest_framework import serializers
from .models import Medication, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'interval_hours', 'is_active']

class MedicationSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)
    next_dose = serializers.ReadOnlyField(source='next_dose_time')

    class Meta:
        model = Medication
        # Add 'last_taken' here
        fields = ['id', 'name', 'dosage', 'current_stock', 'schedules', 'next_dose', 'last_taken']