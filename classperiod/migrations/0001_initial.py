# Generated by Django 5.0.7 on 2024-07-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.CharField(max_length=20)),
                ('class_room', models.CharField(max_length=20)),
            ],
        ),
    ]
