from django.contrib import auth
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import api
# from rest_framework.authentication import TokenAuthentication
from crud.models import Patient
# from gene.models import Genes, Variants

from .serializer import PatientSerializer


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


# @api_view(['GET'])
# def get_genes(request):
#     genes = Genes.objects.all()
#     serializer = GenesSerializer(genes, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_variants(request):
#     variants = Variants.objects.all()
#     serializer = VariantsSerializer(variants, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def add_data(request):
#     serializer = VariantsSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     else:
#         print("there is a problem")

#     return Response(serializer.data)


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
