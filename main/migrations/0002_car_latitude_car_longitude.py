# Generated by Django 5.1.7 on 2025-05-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
