# from django.http import HttpRequest
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from blogs.models import blogs
# from .serializer import BlogsSerializer


@api_view(['GET', 'POST'])
def api_details_blog_view(request):
    res = [{'name': 'Summit', 'id': '123'}]
    return Response(res)
