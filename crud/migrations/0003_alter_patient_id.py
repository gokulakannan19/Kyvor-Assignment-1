# Generated by Django 3.2.9 on 2021-11-08 05:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20211108_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
