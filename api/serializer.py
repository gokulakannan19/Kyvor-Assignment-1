from rest_framework import serializers
from crud.models import Patient
from users.models import Profile
from genome.models import Gene
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'blood_group']


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = "__all__"
