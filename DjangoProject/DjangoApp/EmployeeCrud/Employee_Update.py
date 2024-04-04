from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser  # Importing JSONParser for parsing JSON data
from ..serializers import EmployeePostSerializer
from ..models import EmplloyeeModel


class EmployeeUpdateApi(generics.GenericAPIView):
    serializer_class = EmployeePostSerializer

    @parser_classes([JSONParser])
    def put(self, request, *args, id):
        try:
            userdata = EmplloyeeModel.objects.get(id=id)

            s = EmployeePostSerializer(userdata, data=request.data)
            if s.is_valid():
                s.save()
                return Response({
                    'message': 'Employee details updated successfully',
                    'success': True
                }, status=200)
            else:
                return Response({
                    'message': 'Invalid body request',
                    'success': False
                }, status=400)

        except EmplloyeeModel.DoesNotExist as e:
            return Response({
                'message': 'No employee found with this regid',
                'success': False
            }, status=200)

        except Exception as e:
            return Response({
                'message': 'Employee updation failed',
                'success': False
            }, status=500)
