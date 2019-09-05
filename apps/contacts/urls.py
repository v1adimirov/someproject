from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import PersonListView, feedback_view



urlpatterns = patterns('',
    url(r'^$', PersonListView.as_view(), name='contacts'),
    url(r'^feedback/$', feedback_view, name='contacts_feedback_form'),
    url(r'^feedback/success/$', TemplateView.as_view(
            template_name='assets/feedback_success.html'
        ), name='contacts_feedback_success'),
)
