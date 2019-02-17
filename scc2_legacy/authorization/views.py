from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreateForm

from django.http import JsonResponse


class RegistrationFormView(FormView):
    form_class = UserCreateForm
    success_url = '/stereolife/'
    template_name = 'authorization/registration.html'

    def form_valid(self, form):
        form.save()
        self.user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)

def validate_email(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            message = 'This email address already exists!!!'
            data = {'is_taken': message}
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': True})



class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'authorization/login.html'
    success_url = '/stereolife/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)



class LogOutFormView(View):
    def get(self, request):
        logout(request)
        return redirect('index')




# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect('index')
#         else:
#             login_error = 'User not registered/not found'
#             return render(request, 'authorization/login.html', {'login_error': login_error})
#     else:
#         return render(request, 'authorization/login.html', {})
#
# def logout_view(request):
#     logout(request)
#     return redirect('index')
#
# def register_view(request):
#     if request.method == 'POST':
#         newuser_form = UserCreationForm(request.POST)
#         if newuser_form.is_valid():
#             newuser_form.save()
#             cleaned_data = newuser_form.cleaned_data
#             newuser = authenticate(username=cleaned_data['username'], password=cleaned_data['password2'])
#             login(request, newuser)
#             return redirect('index')
#         else:
#             return render(request, 'authorization/registration.html', {'form': newuser_form})
#     else:
#         return render(request, 'authorization/registration.html', {'form': UserCreationForm()})
