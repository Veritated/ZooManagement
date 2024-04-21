from django.contrib import admin

from .models import *

admin.site.register(Species)
admin.site.register(HealthCondition)

class AnimalInline(admin.TabularInline):
    model = Animal
    extra = 0

@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    inlines = [AnimalInline]

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'birth_date', 'death_date', 'exhibit')
    list_filter = ('species', 'exhibit')

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('animal', 'health_condition', 'date', 'treatment_status')

@admin.register(FeedingAppointment)
class FeedingAppointmentAdmin(admin.ModelAdmin):
    list_display = ('exhibit', 'day', 'time')
    
@admin.register(FeedingAction)
class FeedingActionAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'time')