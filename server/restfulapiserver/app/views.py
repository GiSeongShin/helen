from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from app.models import App
from app.serializers import AppSerializer
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def init_main_page(request):
    if request.method == 'GET':
        result_set = App.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            result_set = result_set.filter(title__icontains=title)

        tutorials_serializer = AppSerializer(result_set, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


# @api_view(['PUT'])
# def add_campaign(request):
# 	request_data = JSONParser().parse(request)
#     request_serializer = AppSerializer()
# 	return JsonResponse()