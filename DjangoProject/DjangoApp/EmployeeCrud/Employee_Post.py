from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import EmployeePostSerializer
from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class EmployeePostApi(generics.GenericAPIView):
    serializer_class = EmployeePostSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            print('hai')
            serializer.is_valid(raise_exception=True)
            print('hai2')
            user = serializer.save()
            print("hai3")
            return Response({
                'message': 'Successful',
                'Result': EmployeePostSerializer(user).data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })