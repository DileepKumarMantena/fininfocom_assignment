from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import EmployeePostSerializer
from ..models import EmplloyeeModel
from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))

class DeleteEmployeeApi(generics.GenericAPIView):
    serializer_class = EmployeePostSerializer

    def delete(self, request, id, format=None):
        try:
            employee = EmplloyeeModel.objects.get(id=id)
            employee.delete()
            return Response({
                'message': 'Employee deleted successfully',
                'success': True
            }, status=200)
        except EmplloyeeModel.DoesNotExist as e:
            return Response({
                'message': 'No employee found with this regid',
                'success': False
            }, status=200)
        except Exception as e:
            return Response({
                'message': 'Employee deletion failed',
                'success': False
            }, status=500)
