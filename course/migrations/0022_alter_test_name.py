# Generated by Django 4.1.2 on 2022-10-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_rename_given_by_test_given_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
