from django.db import models


class Genes(models.Model):
    gene = models.CharField(max_length=200, null=True, blank=True)
    key = models.CharField(max_length=100, primary_key=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gene


class Variants(models.Model):
    variant = models.CharField(max_length=200, null=True, blank=True)
    associated_with_drug_resistance = models.CharField(
        max_length=200, null=True, blank=True)
    protein_effect = models.CharField(
        max_length=200, null=True, blank=True)
    impact = models.CharField(max_length=200, null=True, blank=True)
    variant_description = models.TextField(null=True, blank=True)
    gene = models.ForeignKey(Genes, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.variant
