# Generated by Django 3.0.2 on 2020-02-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='picture_url',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
