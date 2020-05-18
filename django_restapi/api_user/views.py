from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppUserSerializer
from rest_framework import status
from.models import AppUser

# Create your views here.
class AppUserView(APIView):
    def post(self, request):
        appuser_serializer = AppUserSerializer(data=request.data)

        if appuser_serializer.is_valid():
            appuser_serializer.save()
            return Response(appuser_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(appuser_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            appuser_queryset = AppUser.objects.all()
            appuser_queryset_serializer = AppUserSerializer(appuser_queryset, many=True)
            return Response(appuser_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            appuser_serializer = AppUserSerializer(AppUser.objects.get(pk=uid))
            return Response(appuser_serializer.data, status=status.HTTP_200_OK) #테스트용 response

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = AppUser.objects.get(pk=uid)

            update_user_serializer = AppUserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return  Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            uid = kwargs.get('uid')
            user_object = AppUser.objects.get(pk=uid)
            user_object.delete()
            return Response("ok", status=status.HTTP_201_CREATED)