# Generated by Django 5.0.2 on 2024-02-14 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0011_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 14, 13, 4, 35, 319586, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
