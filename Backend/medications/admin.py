from django.contrib import admin
from .models import Medication, Schedule, DoseLog


# This allows you to add/edit schedules directly on the Medication page!
class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1  # Shows 1 empty row by default

# This class "decorates" the Medication admin page
@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('name', 'user', 'dosage', 'current_stock')

    # Add a search bar for name
    search_fields = ('name',)

    # Add a filter sidebar on the right
    list_filter = ('name','user','dosage','current_stock')

    inlines = [ScheduleInline]


# You can still register Schedule separately if you want a dedicated list
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('medication', 'start_time', 'interval_hours', 'is_active')
    list_filter = ('is_active', 'interval_hours')

admin.site.register(DoseLog)