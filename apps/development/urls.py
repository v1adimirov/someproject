from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import order_view, development_page


urlpatterns = patterns('',
    url(r'^$', development_page, name='development_page'),
    url(r'^order/$', order_view, name='development_order_form'),
    url(r'^order/success/$', TemplateView.as_view(
            template_name='arenda/order_success.html'
        ), name='development_order_success'),
)
