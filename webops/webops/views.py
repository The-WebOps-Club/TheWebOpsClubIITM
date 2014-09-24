from UserProfiles.models import Student
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
	user = request.user
	context = {}
	context['user'] = user
	return render(request, 'index.html', context)