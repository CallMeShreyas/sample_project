# Generated by Django 4.1.2 on 2022-10-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_rename_isenable_student_disabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]