# Generated by Django 4.1.7 on 2023-03-22 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_posted', models.DateField(default=datetime.datetime(2023, 3, 22, 21, 24, 36, 256532, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
