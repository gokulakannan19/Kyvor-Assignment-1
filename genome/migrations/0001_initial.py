# Generated by Django 3.2.9 on 2021-11-09 12:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('gene', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('impact', models.CharField(blank=True, max_length=200, null=True)),
                ('protein_effect', models.CharField(blank=True, max_length=200, null=True)),
                ('variant_description', models.CharField(blank=True, max_length=200, null=True)),
                ('associated_with_drug_resistance', models.CharField(blank=True, max_length=200, null=True)),
                ('variant', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('gene', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='genome.gene')),
            ],
        ),
    ]