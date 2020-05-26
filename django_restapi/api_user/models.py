from django.db import models

# Create your models here.
class AppUser(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    class Meta:
        db_table = 'Appuser'

