from django.db import models

class UserImage(models.Model):
	uimage = models.ImageField(upload_to = 'userimage', default = 'none/no-img.jpg')

	class Meta:
		db_table = 'Userimage'


class UserProfile(models.Model):
	uprofile = models.ImageField(upload_to = 'userprofile', default = 'none/no-img.jpg')

	class Meta:
		db_table = 'Userprofile'