import calendar
from datetime import datetime, time

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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

    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, null=True)

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
    
    @property
    def status(self) -> str:
        # this is lame but whatever
        if self.treatment_status == 't':
            return 'Treated'
        elif self.treatment_status == 'u':
            return 'Untreated'
        else:
            return 'Chronic'
        
    def get_absolute_url(self):
        return reverse("update_diagnosis", kwargs={"pk": self.pk})


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
    
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.exhibit} | {self.weekday} | {self.formatted_time}'
    
    @property
    def was_already_fed(self) -> bool:
        return FeedingAction.objects.filter(appointment=self).count() > 0
    
    @property
    def weekday(self) -> str:
        return calendar.day_name[self.day]
    
    @property
    def formatted_time(self) -> str:
        return self.time.strftime("%#I:%M %p")

class FeedingAction(models.Model):
    date_time = models.DateTimeField(default=datetime.now())
    
    staff = models.ManyToManyField(User)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.exhibit} | {self.formatted_date} {self.formatted_time}'
    
    @property
    def weekday(self) -> str:
        return calendar.day_name[self.date_time.weekday()]

    @property
    def formatted_date(self) -> str:
        return self.date_time.strftime("%b %#d, %Y")

    @property
    def formatted_time(self) -> str:
        return self.date_time.time().strftime("%#I:%M %p")