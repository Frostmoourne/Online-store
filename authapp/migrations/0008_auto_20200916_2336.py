# Generated by Django 3.0.7 on 2020-09-16 18:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20200916_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 18, 18, 36, 11, 887618, tzinfo=utc)),
        ),
    ]