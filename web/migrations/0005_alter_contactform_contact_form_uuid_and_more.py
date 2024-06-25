# Generated by Django 5.0.6 on 2024-06-24 17:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='contact_form_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]