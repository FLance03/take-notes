from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def default_view(request):
    print(request.META.get('REMOTE_ADDR'))
    return HttpResponseRedirect(reverse('users:signin'))
