from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Card

from .forms import CardForm, CheckCardForm

# Create your views here.
class BrowseCardsView(LoginRequiredMixin , View):

    def get(self, request):
        cards = Card.unchecked_user_cards(user=request.user).order_by('-date_created').all()
        form = CardForm()
        return render(request, 'cards/browse.html', context={
            'cards': cards,
            'form': form,
            'host': request.META['HTTP_HOST'],
        })

    def post(self, request):
        form = CardForm({
            'owner': request.user.id,
            'title': request.POST['title'],
            'description': request.POST['description'],
        })
        if form.is_valid():
            card = Card(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                owner_id=request.user.id,
            )
            card.save()
            return HttpResponseRedirect(reverse('cards:browse'))
        else:
            return HttpResponse(status=400)


@login_required
def mark_card(request):
    card_id = QueryDict(request.body).get('card_id')
    form = CheckCardForm({
        'owner_id': request.user.id,
        'card_id': card_id,
    })
    if form.is_valid():
        finished_card = Card.objects.get(id=form.cleaned_data['card_id'])
        finished_card.checked = True
        finished_card.save()
        return HttpResponse(status=200)
    else:
        status_code = form.errors.as_data()['__all__'][0].code
        return HttpResponse(status=status_code)





