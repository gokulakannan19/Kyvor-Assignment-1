from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse

from crud.models import Patient

from .serializer import PatientSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/patients/'},
        {'GET': 'api/patients/id'},
        {'POST': 'api/patients/add'},
        {'UPDATE': 'api/patients/update/id/'},
        {'DELETE': 'api/patients/delete/id/'},
    ]

    return Response(routes)


@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def patient_update(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def patient_delete(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response("Patient successfully deleted")
