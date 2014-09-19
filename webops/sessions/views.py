from django.shortcuts import render, render_to_response, get_object_or_404
from sessions.models import SessionDetails
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User

#from django import newforms as forms
from sessions.forms import SessionForm
# Create your views here.

def index(request):
	upcoming_sessions = SessionDetails.objects.order_by('date')[:5]
	context = {}
	context['upcoming_sessions'] = upcoming_sessions
	context['user'] = request.user
	return render(request, 'sessions/index.html', context)

def create_new(request):
	if request.method == 'POST':
		form = SessionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Session Created Successfully")
	else:
		form = SessionForm()
	context = {}
	context.update(csrf(request))
	context['form'] = form
	return render_to_response('sessions/create.html', context)

def detail(request, SessionDetails_id):
	current_session = get_object_or_404(SessionDetails, pk = SessionDetails_id)
	context = {}
	reg_users = list()
	context['current_session'] = current_session
	reg_list = current_session.users_list.split(',')
	for i in reg_list:
		userid = int(i)
		name = User.objects.get(id = userid)
		reg_users.append(name.username)
	context['reg_users'] = reg_users
	return render(request, 'sessions/detail.html', context)

def join_session(request, SessionDetails_id):
	if request.user.is_authenticated():
		current_user = request.user
		user_id = current_user.id
		current_session = get_object_or_404(SessionDetails, pk = SessionDetails_id)
		current_session.users_list += (','+str(user_id))	
		current_session.save()
		return HttpResponseRedirect("/sessions/")
	else:
		return HttpResponse("Please log in")
