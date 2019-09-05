# coding: utf-8
from django import forms

from .models import Resume, Question


class ResumeForm(forms.ModelForm):

    def clean(self):
        file = self.cleaned_data.get('file')

        if not file:
            not_file_required = ['first_name','last_name',
                                 'phone','email','experience']
            for field in not_file_required:
                if not self.cleaned_data.get(field):
                    self._errors[field] = self.error_class(
                        [u'Обязательное поле.']
                    )

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'last_name': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'phone': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'email': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'experience': forms.Textarea(attrs={'class': 'ps-contact-field__input'}),
            'file': forms.ClearableFileInput(attrs={'class': 'file__input'}),
        }

class QuestionForm(forms.ModelForm):

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

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'last_name': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'phone': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'email': forms.TextInput(attrs={'class': 'ps-contact-field__input'}),
            'question': forms.Textarea(attrs={'class': 'ps-contact-field__input'}),
        }

