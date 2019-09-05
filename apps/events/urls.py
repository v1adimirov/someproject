from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import EventDetailView, order_export


urlpatterns = patterns('',
    url(r'^$', EventDetailView.as_view(), name='events_event_detail'),
    #url(r'^success/$', TemplateView.as_view(
    #        template_name='events/eventorder_success.html'
    #    ), name='events_eventorder_success'),
    url(r'^export/(?P<pk>\d+)/$', order_export, name='events_eventorder_export'),
)
