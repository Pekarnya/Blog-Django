# Generated by Django 4.1.7 on 2023-04-05 22:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2023, 4, 5, 22, 28, 8, 712598, tzinfo=datetime.timezone.utc)),
        ),
    ]
