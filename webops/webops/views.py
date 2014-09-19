from UserProfiles.models import Student
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
	small_leaders = Student.objects.order_by(score)[:3]
	new_list = list()
	for p in small_leaders:
		name = User.objects.get(id = p.user_id)
		new_list.append(name)
	context = {'small_leaders': small_leaders}
	return render(request, 'index.html', context)