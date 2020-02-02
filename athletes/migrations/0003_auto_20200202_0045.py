# Generated by Django 3.0.2 on 2020-02-02 00:45

import core.utils.file
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_auto_20200201_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='picture_url',
        ),
        migrations.AddField(
            model_name='athlete',
            name='picture',
            field=models.ImageField(default='default-profile.png', upload_to=core.utils.file.get_path_class),
        ),
    ]