import calendar
from datetime import datetime, time

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Species(models.Model):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'species'
    
    def __str__(self) -> str:
        return f'{self.common_name} ({self.scientific_name})'


class Exhibit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    # location?
    
    def __str__(self) -> str:
        return self.name


class HealthCondition(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=255)

    species = models.ForeignKey(Species, on_delete=models.RESTRICT)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.RESTRICT, null=True)

    @property
    def age(self):
        return datetime.date.today() - self.birth_date
    
    def __str__(self) -> str:
        return f'{self.name} ({self.species.common_name})'


class Diagnosis(models.Model):
    date = models.DateField(verbose_name='date diagnosed')

    TREATMENT_STATUSES = (
        ('t', 'Treated'),
        ('u', 'Untreated'),
        ('c', 'Chronic'),
    )

    treatment_status = models.CharField(max_length=1, choices=TREATMENT_STATUSES, default='u')

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    health_condition = models.ForeignKey(HealthCondition, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['treatment_status']
        verbose_name_plural = 'diagnoses'
        
    def __str__(self) -> str:
        return f'{self.animal} - {self.health_condition}'


class FeedingAppointment(models.Model):
    DAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    
    day = models.SmallIntegerField(choices=DAYS)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, )
    
    def __str__(self) -> str:
        return f'{self.exhibit} {calendar.day_name[self.day]} | {time.strftime(self.time, "%#I:%M %p")}'
    
    @property
    def was_already_fed(self) -> bool:
        return FeedingAction.objects.filter(appointment=self).count() > 0

class FeedingAction(models.Model):
    time = models.TimeField()
    
    staff = models.ManyToManyField(User)
    appointment = models.ForeignKey(FeedingAppointment, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.appointment} | {time.strftime(self.time, "%#I:%M %p")}'