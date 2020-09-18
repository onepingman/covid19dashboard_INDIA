# Generated by Django 3.1.1 on 2020-09-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyStateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.TextField(blank=True)),
                ('state_name', models.TextField(blank=True)),
                ('total_corona_cases', models.IntegerField(blank=True)),
                ('confirmed_corona_cases', models.IntegerField(blank=True)),
                ('recovered_corona_cases', models.IntegerField(blank=True)),
                ('deaths_corona_cases', models.IntegerField(blank=True)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
