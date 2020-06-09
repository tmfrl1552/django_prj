from django.db import models

# Create your models here.
class Comments(models.Model):
    itype = models.CharField(max_length=5, primary_key=True)
    ctext = models.TextField()

    class Meta:
        db_table = "Comments"