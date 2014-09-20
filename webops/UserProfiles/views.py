from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from UserProfiles.models import Student, Interests
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from UserProfiles.forms import UserRegisterForm, UserProfileForm, ProfileForm
# Create your views here.
def index(request):
	user_list = Student.objects.order_by('score').reverse()[:5]
	new_list = list()
	for p in user_list:
		name = User.objects.get(id = p.user_id)
		new_list.append(name)
		#an append method has to be used here to append into another list
	context = {}
	context['user'] = request.user
	context['user_list'] = user_list
	return render(request, 'UserProfiles/index.html', context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect("/UserProfiles")
			else:
				return HttpResponse("Your account is disabled")
		else:
			#print "Invalid login details : {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details provided")
	else:
		return render_to_response('UserProfiles/login.html', {}, context)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/UserProfiles/")

def user_register(request):
	#if request.user.is_anonymous():
		user = request.user
		registered = False
		img = None
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			form2 = UserProfileForm(request.POST)
			if form.is_valid and form2.is_valid:
				user = form.save()
				user.set_password(user.password)
				profile = form2.save(commit=False)
				profile.user = user
				print(request.POST)
				#Now we have to add new models corresponding to these new interests__DONE
				new_interests = request.POST["new_interests"]
				existing_interests = Interests.objects.all()
				#We also have to check if it's not already there. Add capitalization stuff
				for i in new_interests.split(','):
					if not i.strip() in existing_interests:
						new_interest = Interests.create(i.strip()) 
						new_interest.save()
				#Now we have to add the respective interests to each of the users. Just indexes will do
				
				#print(request.POST['interests'])
				#imfn = pjoin(MEDIA_ROOT, user.photo.name)
				#im = PImage.open(imfn)
				#im.thumbnail((160,160), PImage.ANTIALIAS)
				#im.save(imfn, "JPEG") 
				#interest_list = request.POST.getlist('interests')
				#new_list = list()
				#for i in interest_list:
					#new_list.append(str(i))
				#What you have to do is convert these bloody integers to strings
				#newest_list = ",".join(new_list)
				#profile.interests = newest_list
				profile.save()
				registered = True
				return HttpResponse("User Created Successfully.")
		else:
			form = UserRegisterForm()
			form2 = UserProfileForm()
		context = {}
		context.update(csrf(request))
		interests = Interests.objects.all()
		context['interests'] = interests
		context['form'] = form
		context['form2'] = form2
		#context['image'] = "/media/"+ user.photo.name
		#Pass the context to the required template
		return render_to_response('UserProfiles/register.html', context)
	#else :
		#return HttpResponseRedirect('/')
def user_detail(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	user = User.objects.get(id = student.user_id)
	return render(request, 'UserProfiles/detail.html', {'user' : user, 'student' : student})

@csrf_exempt
@login_required
def user_edit(request, student_id):
	student = get_object_or_404(Student, pk=student_id)
	#if (request.user.id != student_id):
		#return HttpResponse("Sorry, you don't have permission")
	img = None
	if request.method == "POST":
		pf = ProfileForm(request.POST, request.FILES, instance=student)
		if pf.is_valid():
			pf.save()
			# resize and save image under same filename
			imfn = pjoin(MEDIA_ROOT, student.photo)
			im = PImage.open(imfn)
			im.thumbnail((160,160), PImage.ANTIALIAS)
			im.save(imfn, "JPEG")
	else:
		pf = ProfileForm(instance=student)

	if student.photo:
		img = "/media/" + student.photo.name
	context = {}
	context.update(csrf(request))
	context['pf'] = pf
	context['img'] = img
	context['user'] = request.user
	return render_to_response("UserProfiles/edit.html", context)