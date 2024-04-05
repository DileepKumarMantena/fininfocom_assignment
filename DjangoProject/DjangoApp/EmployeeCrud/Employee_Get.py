from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import EmployeeGetSerializer
from ..models import EmplloyeeModel

from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class EmployeeGetApi(generics.GenericAPIView):
    serializer_class = EmployeeGetSerializer

    def get(self, request, *args, **kwargs):
        try:
            data = EmplloyeeModel.objects.all()
            serializer_class = EmployeeGetSerializer(data, many=True)
            return Response({'Message': 'Successful',
                             'Result': serializer_class.data,
                             'HasError': False,
                             'Status': 200})

        except Exception as e:
            return Response({'Message': 'Fail',
                             'Result': [],
                             'HasError': True,
                             'Status': 400})
        

