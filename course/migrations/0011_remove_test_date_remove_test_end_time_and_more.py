# Generated by Django 4.1.2 on 2022-10-19 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_alter_test_date_alter_test_end_time_and_more'),
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