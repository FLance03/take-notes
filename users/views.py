from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm

from django.contrib.auth import authenticate, login


# Create your views here.
class SignInView(LoginView):
    template_name = 'users/signin.html'
    next_page = reverse_lazy('cards:browse')
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class LogOutView(LogoutView):
    next_page = reverse_lazy('users:signin')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            user.save()
            return HttpResponseRedirect(reverse('users:signin'))
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


