from .serializers import UserimageSerializer, UserprofileSerializer
from rest_framework.generics import (CreateAPIView)
from rest_framework.response import Response
from rest_framework import status
from .models import UserImage, UserProfile


class UserimageCreateAPIView(CreateAPIView):
	serializer_class = UserimageSerializer
	queryset = UserImage.objects.all()

class UserprofileCreateAPIView(CreateAPIView):
	serializer_class = UserprofileSerializer
	queryset = UserProfile.objects.all()