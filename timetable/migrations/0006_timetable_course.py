# Generated by Django 5.0.2 on 2025-02-25 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_remove_timetable_room_timetable_classroom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.course'),
        ),
    ]
