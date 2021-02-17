from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': mark_safe(room_name),
        'username': mark_safe(request.user.username),
    })