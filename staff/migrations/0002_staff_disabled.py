# Generated by Django 4.1.2 on 2022-10-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
