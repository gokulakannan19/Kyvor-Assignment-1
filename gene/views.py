from django.shortcuts import render, redirect
from django.http import HttpResponse


def get_genes(request):
    return HttpResponse("hi")
