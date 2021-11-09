from django.shortcuts import render
from .models import Gene, Variant
# Create your views here.
def get_genes(request):
    genes = Gene.objects.all()
    context = {

    }
    return render(request, "genome/gene_list.html", context)
