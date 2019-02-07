from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            login_error = 'User not registered/not found'
            return render(request, 'authorization/login.html', {'login_error': login_error})
    else:
        return render(request, 'authorization/login.html', {})


def logout_view(request):
    auth.logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            cleaned_data = newuser_form.cleaned_data
            newuser = auth.authenticate(
                username=cleaned_data['username'],
                password=cleaned_data['password2'],
            )
            auth.login(request, newuser)
            return redirect('index')
        else:
            return render(request, 'authorization/registration.html', {'form': newuser_form})
    else:
        return render(request, 'authorization/registration.html', {'form': UserCreationForm()})
