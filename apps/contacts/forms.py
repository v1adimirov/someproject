# coding: utf-8
from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    is_agree = forms.BooleanField(required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        if not email and not phone:
            self._errors['email'] = self.error_class(
                [u'Обязательное поле.']
            )
            self._errors['phone'] = self.error_class(
                [u'Обязательное поле.']
            )
        return self.cleaned_data

    class Meta:
        model = Feedback
        fields = ['full_name', 'email', 'phone', 'text']
