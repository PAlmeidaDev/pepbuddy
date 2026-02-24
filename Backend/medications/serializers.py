from rest_framework import serializers
from .models import Medication, Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'interval_hours', 'is_active']

class MedicationSerializer(serializers.ModelSerializer):
    # Mantém isto porque a tua @property no model chama-se next_dose_time
    next_dose = serializers.ReadOnlyField(source='next_dose_time')

    class Meta:
        model = Medication
        # Verifica se todos estes campos existem agora no seu models.py
        fields = ['id', 'name', 'dosage', 'current_stock', 'last_taken', 'hours_between_doses', 'next_dose']