# Generated by Django 5.0.2 on 2025-03-06 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_timetable_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.faculty'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='TimetableEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classroom', models.CharField(blank=True, max_length=50, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.course')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.faculty')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.subject')),
            ],
            options={
                'unique_together': {('faculty', 'day', 'start_time')},
            },
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
