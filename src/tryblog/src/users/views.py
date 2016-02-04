from django.shortcuts import render, redirect
from .forms  import ProfileForm
from .models import CustomUser
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from tryblog import settings


# Create your views here.
def cabinet(request):
	
	args = {}
	args['profile_user'] = CustomUser.objects.filter(pk = request.user.pk)
	
	return render(request, 'cabinet.html', args)


def update_user(request):

	profile = CustomUser.objects.get(pk=request.user.pk)

	if request.POST:
		form = ProfileForm(request.POST, request.FILES or None, instance=profile)
		if form.is_valid:
			form.save()
	else:
		form = ProfileForm(instance=profile)

	return render(request, 'update_user.html', {'form':form})


def get_user(request, customuser_pk):

	profile_user = CustomUser.objects.filter(pk=customuser_pk)

	return render(request, 'get_user.html', 
		{'profile_user' : profile_user})



def users(request):

	users = CustomUser.objects.all()

	return render(request, 'users.html',
		{'users':users})