# Generated by Django 4.1.2 on 2022-10-19 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_test_date_test_end_time_test_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='date',
        ),
        migrations.RemoveField(
            model_name='test',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='test',
            name='start_time',
        ),
    ]
