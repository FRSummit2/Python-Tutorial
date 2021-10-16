from django.shortcuts import render

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import render

from .models import employees
from .serializer import employeeSerializer


class EmployeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serialize = employeeSerializer(data=request.data)
        try:
            if serialize.is_valid():
                serialize.save()
                return Response(data=serialize.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        emp = employees.objects.get(id=request.data['id'])
        print(emp)
        serialize = employeeSerializer(emp, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        # emp = employees.objects.get(id=11)
        emp = employees.objects.get(id=request.data['id'])
        emp.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)


@api_view(['GET', 'POST'])
def get_employee_list(request):
    employees1 = employees.objects.all()
    serializer = employeeSerializer(employees1, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
def get_employee_data_from_user(request):
    print('Hello .............. ')
    # dt = request.data
    serializer = employeeSerializer(data=request.data)
    print(serializer)
    # print(json.)
    if request.method == "POST":
        print(request.data)
        print(request.POST['firstName'])
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            # return Response({'data': request.data})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def update_employee_data_from_user(request, slug):
    try:
        employee = employees.objects.get(slug=slug)
    except employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = employeeSerializer(employee, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def employee_template(request):
    return render(request, "employee.html")


def employee_template_ind(request):
    return HttpResponse("Index")
