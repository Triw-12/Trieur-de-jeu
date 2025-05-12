from django.shortcuts import render, redirect

from django.conf import settings
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required

from authentification import forms
from django.forms import ValidationError

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

def login_custom(request):
    form = forms.LoginForm()
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentification/login.html', context={'form': form})

@login_required
def reset_password(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.ResetPasswordForm()
    message = ''
    if request.method == 'POST':
        form = forms.ResetPasswordForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']

            if not request.user.check_password(old_password):
                message = 'Ancien mot de passe incorrect.'
            elif new_password != confirm_password:
                message = 'Les nouveaux mots de passe ne correspondent pas.'
            else:
                try:
                    validate_password(new_password, user=request.user)
                except ValidationError as e:
                    message = ' '.join(e.messages)
                else:
                    request.user.set_password(new_password)
                    request.user.save()
                    message = 'Mot de passe mis à jour avec succès.'
                    return redirect('login')

    return render(request, 'authentification/reset_password.html', context={'form': form, 'message': message})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')
    return render(request, 'authentification/delete_account.html')