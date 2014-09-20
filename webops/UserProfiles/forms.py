from django import forms
from django.contrib.auth.models import User
from UserProfiles.models import Student
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', )

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('rollno', 'writeup', 'photo')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["user", "writeup", "score"]