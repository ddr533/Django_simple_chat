from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Room, Message


@login_required
def get_room_list(request):
    room_list = Room.objects.all()
    return render(request, 'room/room_list.html', {'room_list': room_list})

@login_required
def get_room_detail(request, room_slug):
    room = get_object_or_404(Room, slug=room_slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html', {'room': room,
                                              'messages': messages})

