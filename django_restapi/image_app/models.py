import os
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class OverwriteStorate(FileSystemStorage):
	def get_available_name(self, name, max_length=None):
		if self.exists(name):
			os.remove(os.path.join(settings.MEDIA_ROOT, name))
		return name

class UserImage(models.Model):
	uimage = models.ImageField(upload_to = 'userimage', default = 'none/no-img.jpg', storage=OverwriteStorate())

	class Meta:
		db_table = 'Userimage'


class UserProfile(models.Model):
	uprofile = models.ImageField(upload_to = 'userprofile', default = 'none/no-img.jpg', storage=OverwriteStorate())

	class Meta:
		db_table = 'Userprofile'