# Generated by Django 5.0.3 on 2024-05-03 22:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0011_alter_animal_exhibit_alter_animal_species_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedingaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 17, 39, 51, 394929)),
        ),
    ]
