from django.db import models

# Create your models here.
#from django_restapi.api_user.models import AppUser


class Children(models.Model):
    uid = models.ForeignKey('api_user.AppUser', on_delete=models.CASCADE, db_column='uid')
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=60)

    class Meta:
        db_table = 'Children'