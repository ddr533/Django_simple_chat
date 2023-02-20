from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('core:frontpage')
    return render(request, 'core/signup.html', {'form': form})

def room(request):
    user = request.user.username
    return HttpResponse(content=f'<h1>Привет {user}</h1>')
