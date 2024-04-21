# Generated by Django 5.0.3 on 2024-04-11 02:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HealthCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('exhibit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='zoo.exhibit')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='zoo.species')),
            ],
        ),
        migrations.CreateModel(
            name='FeedingAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('time', models.TimeField()),
                ('animals', models.ManyToManyField(to='zoo.animal')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No'), ('c', 'Chronic')], default='n', max_length=1)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.animal')),
                ('health_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zoo.healthcondition')),
            ],
        ),
    ]
