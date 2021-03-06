# Generated by Django 3.1.13 on 2021-09-03 03:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefibLocationNI',
            fields=[
                ('date_added', models.DateField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=240)),
                ('location_lat', models.CharField(max_length=240)),
                ('location_long', models.CharField(max_length=240)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
