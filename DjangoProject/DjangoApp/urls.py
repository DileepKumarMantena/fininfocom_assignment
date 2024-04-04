from django.urls import path
from .views import *

urlpatterns = [
    path('EmployeePostApi/', EmployeePostApi.as_view()),
    path('EmployeeGetApi/', EmployeeGetApi.as_view()),
    path('EmployeeUpdateApi/', EmployeeUpdateApi.as_view()),
    path('EmployeeDelete/', DeleteEmployeeApi.as_view()),

]