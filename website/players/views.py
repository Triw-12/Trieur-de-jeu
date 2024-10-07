from django.shortcuts import render, redirect

from django.conf import settings
from django.contrib.auth import login

from . import forms

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'players/signup.html', context={'form': form})
