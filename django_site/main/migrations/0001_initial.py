# Generated by Django 4.1.3 on 2022-12-03 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_time', models.CharField(max_length=10)),
                ('is_paid', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(default=None)),
            ],
            options={
                'verbose_name': 'Встреча',
                'verbose_name_plural': 'Встречи',
            },
        ),
    ]
