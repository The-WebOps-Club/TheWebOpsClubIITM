from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SessionDetails(models.Model):
	author = models.ForeignKey(User)
	date = models.DateField()
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 500)
	skills = models.CommaSeparatedIntegerField(max_length = 10)
	users_list = models.CommaSeparatedIntegerField(max_length = 1000)
	def __str__(self):
		return self.title
