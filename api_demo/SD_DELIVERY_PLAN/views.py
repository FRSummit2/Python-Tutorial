from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import render

import requests

from django.db import connection

from .models import DeliveryPlan
from .serializer import DeliveryPlanSerializer

cursor = connection.cursor()


class DeliveryPlanController(APIView):

    def get(self, request):
        print('............................................')
        print(cursor)
        sql = 'SELECT * FROM sd_delivery_plan_deliveryplan'
        try:
            cursor.execute(sql)
            row = cursor.fetchall()
            for record in row:
                print(record)
        except Exception as e:
            print(e)
        print('............................................')
        dp = DeliveryPlan.objects.all()
        serializer = DeliveryPlanSerializer(dp, many=True)

        return Response(serializer.data)

    def post(self, request):
        serialize = DeliveryPlanSerializer(data=request.data)
        try:
            if serialize.is_valid():
                serialize.save()
                return Response(data=serialize.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        dp = DeliveryPlan.objects.get(id=request.data['id'])
        serialize = DeliveryPlanSerializer(dp, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        dp = DeliveryPlan.objects.get(id=request.data['id'])
        dp.delete()
        return Response(data='Delete', status=status.HTTP_410_GONE)


@api_view(['GET', 'POST'])
def get_external_api_data(request):
    response = requests.get('http://frs-json-server.herokuapp.com/jerp_menu').json()
    return Response(response)

