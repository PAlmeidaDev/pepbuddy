from rest_framework import serializers
from .models import Medication, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'interval_hours', 'is_active']

class MedicationSerializer(serializers.ModelSerializer):
    # This nesting shows the schedules inside the medication JSON!
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Medication
        fields = ['id', 'name', 'dosage', 'current_stock', 'schedules']