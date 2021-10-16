from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
from django.shortcuts import render


from django.db import connection

cursor = connection.cursor()

class DeliveryPlanController(APIView):

    def get(self, request):
        print('------------------------------------------')
        print(cursor)
        sql = 'SELECT * FROM SD_DELIVERY_PLAN'
        try:
            cursor.execute(sql)
            row = cursor.fetchall()
            for record in row:
                print(record)
        except Exception as e:
            print(e)
        print('............................................')

        return Response({'data': 'serializer.data'})
