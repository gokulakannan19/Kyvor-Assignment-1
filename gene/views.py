from django.shortcuts import render
from django.http import HttpResponse

from .models import Genes, Variants


def get_genes(request):
    genes = Genes.objects.all()
    context = {
        'genes': genes
    }
    return render(request, "gene/gene_list.html", context)


def gene_detail(request, pk):
    gene = Genes.objects.get(key=pk)
    variants = gene.variants_set.all()

    context = {
        'gene': gene,
        'variants': variants,
    }

    return render(request, "gene/gene_detail.html", context)


def variant_detail(request, pk):
    variant = Variants.objects.get(id=pk)

    context = {
        "variant": variant,
    }

    return render(request, "gene/variant_detail.html", context)
