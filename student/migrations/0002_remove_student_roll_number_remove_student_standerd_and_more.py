# Generated by Django 4.1.2 on 2022-10-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='standerd',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]