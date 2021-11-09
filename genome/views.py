from django.shortcuts import render
from .models import Gene, Variant
# Create your views here.


def get_genes(request):
    genes = Gene.objects.all()
    context = {

    }
    return render(request, "genome/gene_list.html", context)


def gene_detail(request, pk):
    gene = Gene.objects.get(id=pk)
    variants = gene.variant_set.all()
    context = {
        'gene': gene,
        'variants': variants,

    }
    return render(request, "geneome/gene_detail.html", context)


def variant_detail(request, pk):
    variant = Variant.objects.get(id=pk)

    context = {

        'variant': variant,

    }
    return render(request, "geneome/variant_detail.html", context)
