# Generated by Django 3.0.2 on 2020-02-02 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
        ('participations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participation',
            name='modality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.Modality'),
            preserve_default=False,
        ),
    ]
