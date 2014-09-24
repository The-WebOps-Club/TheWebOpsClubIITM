from django.shortcuts import render, render_to_response, get_object_or_404
from project.models import ProjectDetails
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User

#from django import newforms as forms
from project.forms import ProjectForm
# Create your views here.

def index(request):
	projects = ProjectDetails.objects.all()
	context = {}
	context['projects'] = projects
	context['user'] = request.user
	return render(request, 'project/index.html', context)

def create_new(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit = False)
			project.author = user
			project.save()
			return HttpResponse("Project Created Successfully")
	else:
		form = ProjectForm()
	context = {}
	context.update(csrf(request))
	context['form'] = form
	return render_to_response('project/create.html', context)

def detail(request, ProjectDetails_id):
	current_project = get_object_or_404(ProjectDetails, pk = ProjectDetails_id)
	context = {}
	reg_users = list()
	context['current_project'] = current_project
	reg_list = current_project.users_list.split(',')
	for i in reg_list:
		userid = int(i)
		name = User.objects.get(id = userid)
		reg_users.append(name.username)
	context['reg_users'] = reg_users
	return render(request, 'project/detail.html', context)

def join_project(request, ProjectDetails_id):
	if request.user.is_authenticated():
		current_user = request.user
		user_id = current_user.id
		current_project = get_object_or_404(ProjectDetails, pk = ProjectDetails_id)
		current_project.users_list += (','+str(user_id))	
		current_project.save()
		return HttpResponseRedirect("/project/")
	else:
		return HttpResponse("Please log in")
