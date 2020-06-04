from django.db import models

class UserImage(models.Model):
	uimage = models.ImageField(upload_to = '', default = 'none/no-img.jpg')

	class Meta:
		db_table = 'Userimage'
