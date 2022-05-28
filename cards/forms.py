from django import forms
from django.core.exceptions import ValidationError

from .models import Card

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ['title', 'description', 'owner']


class CheckCardForm(forms.Form):
    card_id = forms.IntegerField()
    owner_id = forms.IntegerField()

    def clean(self):
        try:
            card = Card.objects.get(pk=self.cleaned_data['card_id'])
        except Card.DoesNotExist:
            raise ValidationError("Card with the given id does not exist", code=404)
        else:
            if card.owner_id != self.cleaned_data['owner_id']:
                raise ValidationError("Authorization failed", code=403)