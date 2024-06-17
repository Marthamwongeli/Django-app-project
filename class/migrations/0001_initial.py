# Generated by Django 5.0.6 on 2024-06-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=20)),
                ('room_number', models.PositiveSmallIntegerField()),
                ('class_size', models.IntegerField()),
                ('start_time', models.CharField(max_length=28)),
                ('end_time', models.CharField(max_length=20)),
                ('school_year', models.IntegerField()),
                ('description', models.TextField(max_length=50)),
                ('created_at', models.CharField(max_length=20)),
            ],
        ),
    ]