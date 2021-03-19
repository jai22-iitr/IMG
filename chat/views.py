from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Message 
from django.utils.safestring import mark_safe
import json


def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
	else:
			form = UserCreationForm()	
	return render(request,'registration/register.html', {'form':form})
	
@login_required(login_url='/login')
def index(request):
	roomnames=Message.objects.all().values('room').distinct()
	print(roomnames)
	return render(request, 'chat/dashboard.html',{'roomnames':roomnames})


@login_required(login_url='/login')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': mark_safe(room_name),
        'username': mark_safe(request.user.username),
    })



