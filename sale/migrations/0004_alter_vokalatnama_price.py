# Generated by Django 5.2.1 on 2025-05-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_alter_vokalatnama_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vokalatnama',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
