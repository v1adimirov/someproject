# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from .models import SaleObject, Contacts



class SaleListView(ListView):

    def get_context_data(self, **kwargs):
        kwargs.update({
            'managers': Contacts.objects.all(),
        })
        return super(SaleListView, self).get_context_data(**kwargs)

urlpatterns = patterns('',
    url(r'^$', SaleListView.as_view(model=SaleObject), name='sale_saleobject_list'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=SaleObject), name='sale_saleobject_detail'),
)
