# Generated by Django 4.1.7 on 2023-04-23 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_unique_id_alter_post_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2023, 4, 23, 12, 10, 19, 613207, tzinfo=datetime.timezone.utc)),
        ),
    ]
