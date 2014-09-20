from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
	photo = models.ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
	user = models.OneToOneField(User, primary_key=True)
	writeup = models.TextField(max_length = 200)
	score = models.IntegerField(default = 0)
	rollno = models.CharField(max_length = 8)
	#image = models.ImageField()
	interests = models.TextField(max_length=100)
	def __str__(self):
		no = self.user_id
		return User.objects.get(id=no).username

class Interests(models.Model):
	interest = models.CharField(max_length = 20)

	def __str__(self):
		return self.interest

	@classmethod
	def create(cls, title):
		interest_instance = cls(interest = title)
		return interest_instance