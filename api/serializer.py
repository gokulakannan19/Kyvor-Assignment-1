from rest_framework import serializers
from crud.models import Patient
from users.models import Profile
from gene.models import Genes, Variants
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'blood_group']


class GenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genes
        fields = "__all__"


class VariantsSerializer(serializers.ModelSerializer):
    gene = GenesSerializer(many=False)

    class Meta:
        model = Variants
        fields = "__all__"
