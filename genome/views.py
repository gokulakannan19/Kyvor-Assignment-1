from re import S, search
from django.core import paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Gene
from .filters import GeneFilter
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
    # my_filter = GeneFilter(request.GET, queryset=genes)
    # genes = my_filter.qs

    variant_list = []
    for gene in genes:
        if gene.variant not in variant_list:
            variant_list.append(gene)

    context = {
        "gene": pk,
        "variant_list": variant_list,
        # "my_filter": my_filter,

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
