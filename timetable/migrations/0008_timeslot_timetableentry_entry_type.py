# Generated by Django 5.0.2 on 2025-03-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_remove_faculty_subject_subject_faculty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='timetableentry',
            name='entry_type',
            field=models.CharField(choices=[('Lecture', 'Lecture'), ('Lab', 'Lab'), ('Break', 'Break')], default='Lecture', max_length=10),
        ),
    ]
