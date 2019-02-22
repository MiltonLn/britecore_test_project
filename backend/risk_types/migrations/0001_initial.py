# Generated by Django 2.1.7 on 2019-02-22 02:00

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('fields_type', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
