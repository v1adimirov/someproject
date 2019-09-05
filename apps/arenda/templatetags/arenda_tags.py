from django.template import Library

from arenda.models import Contacts, Mart
from arenda.forms import OrderForm


register = Library()


@register.inclusion_tag('arenda/tags/contacts_list.html')
def contacts_list():
    return {
        'old_list': Contacts.objects.filter(is_old=True),
        'new_list': Contacts.objects.filter(is_new=True)
    }


@register.inclusion_tag('arenda/order_form.html')
def order_form():
    return {
        'form': OrderForm()
    }


@register.inclusion_tag('arenda/tags/slider.html')
def arenda_slider(request_path=None):
    qs = Mart.objects.filter(is_active=True).exclude(image__isnull=True)
    if request_path is not None:
        qs = qs.exclude(link=request_path)
        qs = qs.exclude(link='http://maxi-cre.ru' + request_path)
    return {
        'object_list': qs
    }
