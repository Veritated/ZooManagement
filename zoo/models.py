import datetime

from django.db import models

# Create your models here.

class Species(models.Model):
    common_name = models.CharField()
    scientific_name = models.CharField()


class Exhibit(models.Model):
    name = models.CharField()
    description = models.CharField()
    # location?


class HealthCondition(models.Model):
    name = models.CharField()
    description = models.CharField()


class Animal(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    description = models.CharField()

    species = models.ForeignKey(Species, on_delete=models.RESTRICT)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.RESTRICT, null=True)

    @property
    def get_age_today(self):
        return datetime.date.today() - self.birth_date


class Diagnosis(models.Model):
    date = models.DateField()

    RESOLUTIONS = (
        ('y', 'Yes'),
        ('n', 'No'),
        ('c', 'Chronic'),
    )

    is_resolved = models.CharField(max_length=1, choices=RESOLUTIONS, blank=True, default='n')

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    health_condition = models.ForeignKey(HealthCondition, on_delete=models.CASCADE)
