from django.shortcuts import render

# Create your views here.
from .EmployeeCrud.Employee_Post import EmployeePostApi
from .EmployeeCrud.Employee_Get import EmployeeGetApi
from .EmployeeCrud.Employee_Update import EmployeeUpdateApi
from .EmployeeCrud.Employee_Delete import DeleteEmployeeApi

EmployeePostApi()
EmployeeGetApi()
EmployeeUpdateApi()
DeleteEmployeeApi()
