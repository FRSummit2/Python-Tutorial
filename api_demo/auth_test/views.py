from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import render

from django.db import connection

cursor = connection.cursor()


class AuthTest(APIView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    # def post(self, request):
    #     serialize = DeliveryPlanSerializer(data=request.data)
    #     try:
    #         if serialize.is_valid():
    #             serialize.save()
    #             return Response(data=serialize.data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)
    #
    # def put(self, request):
    #     dp = DeliveryPlan.objects.get(id=request.data['id'])
    #     serialize = DeliveryPlanSerializer(dp, data=request.data)
    #     if serialize.is_valid():
    #         serialize.save()
    #         return Response(data=serialize.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(serialize.errors, status=status.HTTP_404_NOT_FOUND)
    #
    # def delete(self, request):
    #     dp = DeliveryPlan.objects.get(id=request.data['id'])
    #     dp.delete()
    #     return Response(data='Delete', status=status.HTTP_410_GONE)

