# Generated by Django 4.1.7 on 2023-04-24 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_feed_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2023, 4, 24, 13, 52, 20, 569672, tzinfo=datetime.timezone.utc)),
        ),
    ]
