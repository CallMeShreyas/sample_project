# Generated by Django 4.1.2 on 2022-10-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_test_date_alter_test_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_time',
            field=models.TimeField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='start_time',
            field=models.TimeField(blank=True, default=0),
        ),
    ]
