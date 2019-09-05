# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from .models import Vacancy
from .views import VacancyListView, resume_view, question_view

urlpatterns = patterns('',
    # url(r'^$', ListView.as_view(model=Vacancy), name='vacancies_vacancy_list'),
    url(r'^$', VacancyListView.as_view(), name='vacancies_debug'),
    url(r'^resume/$', resume_view, name='resume_view'),
    url(r'^question/$', question_view, name='question_view'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Vacancy), name='vacancies_vacancy_detail'),
)
