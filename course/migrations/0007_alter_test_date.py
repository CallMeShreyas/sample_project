# Generated by Django 4.1.2 on 2022-10-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_test_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(default='0000-00-00'),
        ),
    ]
