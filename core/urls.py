from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.default_view, name='default_view')
]