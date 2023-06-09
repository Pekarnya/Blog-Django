# Generated by Django 4.1.7 on 2023-04-05 22:37

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2023, 4, 5, 22, 37, 24, 797269, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_user',
            field=models.BigIntegerField(null=True),
        ),
    ]
