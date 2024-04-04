from django.apps import apps
from rest_framework import serializers

from .models import *

from django.contrib.auth.hashers import make_password

class EmployeePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmplloyeeModel
        fields = "__all__"

    def create(self, validated_data):
        user = EmplloyeeModel.objects.create(Name=validated_data['Name'],
                                        Email=validated_data['Email'],
                                        Age=validated_data['Age'],
                                        Gender=validated_data['Gender'], 
                                        Phone_No=validated_data['Phone_No'],
                                        Address_Details=validated_data['Address_Details'],
                                        H_No=validated_data['H_No'],
                                        Street=validated_data['Street'],
                                        City=validated_data['City'],
                                        State=validated_data['State'],
                                        Work_Experience=validated_data['Work_Experience'],
                                        Company_Name=validated_data['Company_Name'],
                                        From_Date=validated_data['From_Date'],
                                        To_Date=validated_data['To_Date'],
                                        Address=validated_data['Address'],
                                        Qualifications=validated_data['Qualifications'],
                                        Qualification_Name=validated_data['Qualification_Name'],
                                        Percentage=validated_data['Percentage'],
                                        Projects=validated_data['Projects'],
                                        Title=validated_data['Title'],
                                        Description=validated_data['Description'],
                                        Photo=validated_data['Photo'])

        user.save()
        return user

class EmployeeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmplloyeeModel
        fields = "__all__"