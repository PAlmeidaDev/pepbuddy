from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Medication(models.Model):
    # Relaciona o medicamento ao utilizador (cada um vê só os seus)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50, help_text="Ex: 500mg, 1 comprimido")
    last_taken = models.DateTimeField(blank=True, null=True)

    # Stock atual para avisar quando estiver a acabar
    current_stock = models.IntegerField(default=0)

    hours_between_doses = models.IntegerField(default=8)
    # Metadados úteis para o portefólio
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def next_dose_time(self):
        # Se não houver dose registrada, usamos o "agora" como base de cálculo
        if not self.last_taken:
            # Você pode retornar None ou calcular a partir de 'agora'
            # Vamos usar 'agora' para evitar o erro de 1970 no React
            return timezone.now() + timedelta(hours=self.hours_between_doses)

        # Se existe uma última dose, o cálculo é simples e direto
        return self.last_taken + timedelta(hours=self.hours_between_doses)


class Schedule(models.Model):
    # This links the schedule to one of your medications
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        related_name="schedules"
    )

    # When should the first dose be taken?
    start_time = models.TimeField(help_text="Time of the first dose")

    # Frequency logic
    interval_hours = models.PositiveIntegerField(
        help_text="How many hours between doses? (e.g., 8, 12, 24)"
    )

    # To easily turn a reminder off without deleting it
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medication.name} - Every {self.interval_hours}h"


class DoseLog(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        # This formats it to: "Medication Name - Feb 25, 10:07 PM"
        return f"{self.medication.name} - {self.timestamp.strftime('%b %d, %I:%M %p')}"