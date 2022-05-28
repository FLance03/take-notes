from django.urls import path

from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.BrowseCardsView.as_view(), name='browse'),
    path('check/', views.mark_card, name='mark_card'),
    # path('<int:card_id>/', views.card_detail, name="card_detail"),
]