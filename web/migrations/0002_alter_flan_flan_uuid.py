# Generated by Django 5.0.6 on 2024-06-22 18:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
