from django.db import models
import uuid
# Create your models here.


class Gene(models.Model):
    gene = models.CharField(max_length=200, null=True, blank=True)
    key = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.gene


class Variant(models.Model):
    gene = models.ForeignKey(
        Gene, null=True, blank=True, on_delete=models.CASCADE)
    impact = models.CharField(max_length=200, null=True, blank=True)
    variant_description = models.CharField(
        max_length=200, null=True, blank=True)
    variant = models.CharField(max_length=200, null=True, blank=True)
    protein_effect = models.CharField(max_length=200, null=True, blank=True)
    variant_description = models.CharField(
        max_length=200, null=True, blank=True)
    associated_with_drug_resistance = models.CharField(
        max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.variant
