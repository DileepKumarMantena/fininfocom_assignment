from django.apps import apps
from rest_framework import serializers

from .models import *

from django.contrib.auth.hashers import make_password

class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmplloyeeModel
        fields = "__all__"

    def create(self, validated_data):
        try:
            user = EmplloyeeModel.objects.create(**validated_data)
            return user
        except Exception as e:
            raise serializers.ValidationError(str(e))  
class EmployeeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmplloyeeModel
        fields = "__all__"