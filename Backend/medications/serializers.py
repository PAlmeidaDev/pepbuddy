from rest_framework import serializers
from .models import Medication, Schedule, DoseLog

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'interval_hours', 'is_active']

class DoseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoseLog
        fields = ['id', 'timestamp']

class MedicationSerializer(serializers.ModelSerializer):
    # Add this line to include the last 5 logs for each med
    recent_logs = DoseLogSerializer(source='logs', many=True, read_only=True)
    next_dose = serializers.ReadOnlyField(source='next_dose_time')

    class Meta:
        model = Medication
        fields = ['id', 'name', 'dosage', 'current_stock', 'last_taken', 'hours_between_doses', 'next_dose', 'recent_logs']