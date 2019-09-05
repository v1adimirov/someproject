# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Vacancy, Adv, SliderItem, ContactPerson
from .forms import ResumeForm, QuestionForm

from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# отправка уведомлений на почту
# ибо долго разбираться как работать с mailer
def send_message(template, subject, data, file_path=''):
    template = get_template(template)
    from_email = settings.DEFAULT_FROM_EMAIL
    if data.get('email'):
        headers = {'From': data['email']}
    else:
        headers = {}

    email = EmailMultiAlternatives(subject,
                            template.render(Context(data)),
                            from_email,
                            ['resume@maxi-net.ru',],
                            headers=headers)

    if file_path:
        email.attach_file(file_path)
    email.send()



class VacancyListView(ListView):

    model = Vacancy
    template_name = u"vacancies/vacancy_list_debug.html"

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['advantages'] = Adv.objects.all()[:3]
        context['slides'] = SliderItem.objects.filter(is_active=True)
        context['resume_form'] = ResumeForm()
        context['question_form'] = QuestionForm()
        context['persons'] = ContactPerson.objects.all()
        return context

# обработчик формы резюме
def resume_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save()
            if message.file:
                path = message.file.path
            else:
                path = ''
            send_message(u"vacancies/mail/message.txt",
                         u"Резюме с сайта maxi-cre.ru",
                         form.cleaned_data, path)
            return redirect('arenda_order_success')
    else:
        form = ResumeForm()
    return render(request, 'vacancies/resume_form.html', {
        'form': form,
    })

# обработчик формы вопросы
def question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_message(u"vacancies/mail/question.txt",
                         u"Вопрос с сайта maxi-cre.ru",
                         form.cleaned_data)
            return redirect('arenda_order_success')
    else:
        form = QuestionForm()
    return render(request, 'vacancies/question_form.html', {
        'form': form,
    })