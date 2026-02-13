from django.db import models
from django.contrib.auth.models import User


class Medication(models.Model):
    # Relaciona o medicamento ao utilizador (cada um vê só os seus)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50, help_text="Ex: 500mg, 1 comprimido")

    # Stock atual para avisar quando estiver a acabar
    current_stock = models.IntegerField(default=0)

    # Metadados úteis para o portefólio
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.dosage}"


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