# Generated by Django 3.2.8 on 2021-11-04 17:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 17, 53, 45, 735552, tzinfo=utc)),
        ),
    ]
