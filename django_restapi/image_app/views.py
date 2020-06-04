from .serializers import imageSerializer
from rest_framework.generics import (CreateAPIView)
from .models import UserImage


class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = UserImage.objects.all()