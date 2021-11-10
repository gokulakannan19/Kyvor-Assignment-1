from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Gene
# Create your views here.


def gene_list(request):
    genes = Gene.objects.values_list('gene', flat=True).distinct()
    print(genes)
    context = {

        'genes': genes
    }
    return render(request, 'genome/gene_list.html', context)


@login_required(login_url='login-user')
def gene_detail(request, pk):
    genes = Gene.objects.filter(gene=pk)
    variant_list = []
    for gene in genes:
        if gene.variant not in variant_list:
            variant_list.append(gene)
    context = {
        "gene": pk,
        "variant_list": variant_list
    }

    return render(request, 'genome/gene_detail.html', context)


@login_required(login_url='login-user')
def variant_detail(request, pk):
    variant = Gene.objects.get(id=pk)
    print(variant)
    print(variant.gene)
    context = {

        "variant": variant
    }

    return render(request, 'genome/variant_detail.html', context)
