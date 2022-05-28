from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', views.LogOutView.as_view(), name='logout')
]