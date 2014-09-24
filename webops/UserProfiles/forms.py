from django import forms
from django.contrib.auth.models import User
from UserProfiles.models import Student
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', )
		#widgets = {
			#'first_name' : forms.TextInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'First Name'}),
			#'last_name' : forms.TextInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'Last Name'}),
			#'email' : forms.TextInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'Email'}),
			#'username' : forms.TextInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'Username'}),
			#'password1' : forms.PasswordInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'Password'}),
			#'password2' : forms.PasswordInput(attrs= {'class': 'form-control input-lg', 'placeholder': 'Password'}),
		#}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('rollno', 'writeup', 'photo')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ["user", "writeup", "score"]