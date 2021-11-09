from django.shortcuts import render
from django.http import HttpResponse

from .models import Genes, Variants


def home(request):
    genes = Genes.objects.all()
    context = {
        'genes': genes
    }
    return render(request, "gene/gene_list.html", context)
