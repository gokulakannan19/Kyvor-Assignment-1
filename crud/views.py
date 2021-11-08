from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient


def home(request):
    patients = Patient.objects.all()

    context = {
        'patients': patients,
    }

    return render(request, 'crud/patients.html', context)
