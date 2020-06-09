from rest_framework import serializers

from rest_framework.serializers import (
    ModelSerializer,
)

from .models import UserImage, UserProfile


class UserimageSerializer(ModelSerializer):

    class Meta:
        model = UserImage
        fields = [
            'uimage'
        ]

class UserprofileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'uprofile'
        ]