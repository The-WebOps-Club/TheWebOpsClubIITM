from django.forms import ModelForm
from project.models import ProjectDetails
from django import forms

class ProjectForm(ModelForm):
	class Meta:
		model = ProjectDetails
		fields = ['title', 'description', 'skills']

