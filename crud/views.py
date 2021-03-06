from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm


def home(request):
    patients = Patient.objects.all()

    context = {
        'patients': patients,
    }

    return render(request, 'crud/patients.html', context)


@login_required(login_url='login-user')
def add_patient(request):

    form = PatientForm()

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient')

    context = {
        'form': form
    }
    return render(request, 'crud/patient_form.html', context)


@login_required(login_url='login-user')
def update_patient(request, pk):
    patient = Patient.objects.get(id=pk)

    form = PatientForm(instance=patient)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patient")

    context = {
        'form': form,
    }

    return render(request, 'crud/patient_form.html', context)


@login_required(login_url='login-user')
def delete_patient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == "POST":
        patient.delete()
        return redirect("patient")
    context = {
        'patient': patient,
    }

    return render(request, 'delete-page.html', context)
