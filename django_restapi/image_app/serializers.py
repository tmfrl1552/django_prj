from rest_framework import serializers

from rest_framework.serializers import (
    ModelSerializer,
)

from .models import UserImage


class imageSerializer(ModelSerializer):

    class Meta:
        model = UserImage
        fields = [
            'uimage'
        ]