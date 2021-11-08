from rest_framework import serializers
from crud.models import Patient
from users.models import Profile
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'blood_group']
