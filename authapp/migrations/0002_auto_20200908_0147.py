# Generated by Django 3.0.7 on 2020-09-07 20:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 9, 20, 47, 35, 974755, tzinfo=utc)),
        ),
    ]
