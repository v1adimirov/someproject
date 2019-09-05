from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import order_view, order_export


urlpatterns = patterns('',
    url(r'^order/$', order_view, name='arenda_order_form'),
    url(r'^order/success/$', TemplateView.as_view(
            template_name='arenda/order_success.html'
        ), name='arenda_order_success'),
     url(r'^order/export/$', order_export, name='arenda_order_export'),
)
