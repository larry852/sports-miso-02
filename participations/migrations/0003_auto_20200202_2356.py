# Generated by Django 3.0.2 on 2020-02-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participations', '0002_participation_modality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentary',
            name='datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='participation',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
