from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import EmployeePostSerializer
from rest_framework.parsers import MultiPartParser

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class EmployeePostApi(generics.GenericAPIView):
    serializer_class = EmployeePostSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                'message': 'Employee created successfully',
                'regid': user.regid,
                'success': True
            }, status=200)
        except serializer.ValidationError as e:
            # Duplicate email error
            if 'email' in e.detail and 'unique' in e.detail['email'][0]:
                return Response({
                    'message': 'Employee already exists',
                    'success': False
                }, status=200)
            else:
                return Response({
                    'message': 'Invalid body request',
                    'success': False
                }, status=400)
        except Exception as e:
            # Exception occurred
            return Response({
                'message': 'Employee creation failed',
                'success': False
            }, status=500)
