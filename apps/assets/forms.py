# coding: utf-8
from django import forms

from .models import (
    Feedback, VologdaFeedback, FranchFeedback,
    FranchVologdaFeedback, MartFeedback, FranchMartFeedback
)


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
        fields = ['city', 'full_name', 'email', 'phone', 'text']


class VologdaFeedbackForm(forms.ModelForm):

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
        model = VologdaFeedback
        fields = ['mart', 'full_name', 'email', 'phone', 'text']


class MartFeedbackForm(forms.ModelForm):

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
        model = MartFeedback
        fields = ['mart', 'full_name', 'email', 'phone', 'text']


class FranchCityFeedbackForm(forms.ModelForm):

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
        model = FranchFeedback
        fields = ['franch', 'full_name', 'email', 'phone', 'text']


class FranchVologdaFeedbackForm(forms.ModelForm):

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
        model = FranchVologdaFeedback
        fields = ['franch', 'full_name', 'email', 'phone', 'text']


class FranchMartFeedbackForm(forms.ModelForm):

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
        model = FranchMartFeedback
        fields = ['franch', 'full_name', 'email', 'phone', 'text']
