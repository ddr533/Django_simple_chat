from django.contrib.auth import login
from django.shortcuts import redirect, render

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
