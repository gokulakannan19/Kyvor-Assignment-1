from django.contrib import auth
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from crud.models import Patient
from genome.models import Gene

from .serializer import PatientSerializer, GeneSerializer
from api import serializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': 'api/patients/'},
        {'GET': 'api/patients/id'},
        {'POST': 'api/patients/add'},
        {'UPDATE': 'api/patients/update/id/'},
        {'DELETE': 'api/patients/delete/id/'},

        {'GET': 'api/genes/'},
        {'GET': 'api/genes/id'},
        {'POST': 'api/genes/add'},
        {'POST': 'api/variants/add'},
        {'GET': 'api/variants/id'},
    ]

    return Response(routes)

# -------------------------------------------------------------------------------------------


@api_view(['GET'])
def genes(request):
    genes = Gene.objects.values_list('gene', flat=True).distinct()

    return Response(genes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_genes(request):
    genes = Gene.objects.all()
    serializer = GeneSerializer(genes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gene_detail(request, pk):
    gene = pk
    genes = Gene.objects.filter(gene=pk)
    variant_list = []
    for gene in genes:
        if gene.variant not in variant_list:
            variant_list.append(gene.variant)
    # serializer = GeneSerializer(variant_list, many=True)
    return Response(variant_list)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def variant_detail(request, pk):

    variant = Gene.objects.get(id=pk)
    serializer = GeneSerializer(variant, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def gene_create(request):
    serializer = GeneSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# --------------------------------------------------------------------------------------
@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def patient_create(request):
    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def patient_update(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(instance=patient, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def patient_delete(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response("Patient successfully deleted")
