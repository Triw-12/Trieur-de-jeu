from django.shortcuts import render, redirect

from django.conf import settings
from django.contrib.auth import login, logout

from authentification import forms

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={'form': form})


def logout_custom(request):
    logout(request)
    return redirect('home')
