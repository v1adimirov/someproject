from django import forms

from .models import EventOrder


class EventOrderForm(forms.ModelForm):

    is_agree = forms.BooleanField(required=True)

    def __init__(self, event_obj=None, *args, **kwargs):
        super(EventOrderForm, self).__init__(*args, **kwargs)
        self.event = event_obj
        transfer_qs = self.event.transfers.all()
        if transfer_qs.exists():
            self.fields['transfer'] = forms.ModelChoiceField(queryset=self.event.transfers.all())

    class Meta:
        model = EventOrder
        fields = ['full_name', 'company', 'city', 'brend', 'phone', 'email', 'transfer', 'message']
