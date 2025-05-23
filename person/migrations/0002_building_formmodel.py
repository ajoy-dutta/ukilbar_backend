# Generated by Django 5.2.1 on 2025-05-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=100)),
                ('form_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
    ]
