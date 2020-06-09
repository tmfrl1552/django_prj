from django.db import models

# Create your models here.
class Result(models.Model):
    uid = models.ForeignKey('api_user.AppUser', on_delete=models.CASCADE, db_column='uid')
    name = models.CharField(max_length=20)
    itype = models.ForeignKey('api_comments.Comments', db_column='itype', on_delete=models.PROTECT)
    uimage = models.TextField()
    date = models.CharField(max_length=20)

    class Meta:
        db_table = 'Result'