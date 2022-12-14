# Generated by Django 4.1.2 on 2022-10-18 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0009_alter_student_disabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('course_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('given_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
                ('option_1', models.CharField(max_length=10)),
                ('option_2', models.CharField(max_length=10)),
                ('option_3', models.CharField(max_length=10)),
                ('option_4', models.CharField(max_length=10)),
                ('choosed_anwser', models.CharField(choices=[('1', models.CharField(max_length=10)), ('2', models.CharField(max_length=10)), ('3', models.CharField(max_length=10)), ('4', models.CharField(max_length=10))], max_length=10)),
                ('correct_answer', models.CharField(choices=[('1', models.CharField(max_length=10)), ('2', models.CharField(max_length=10)), ('3', models.CharField(max_length=10)), ('4', models.CharField(max_length=10))], max_length=10)),
                ('test_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.test')),
            ],
        ),
    ]
