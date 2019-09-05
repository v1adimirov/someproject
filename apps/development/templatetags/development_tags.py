from django.template import Library

from development.forms import OrderForm


register = Library()


@register.inclusion_tag('development/order_form.html')
def order_form():
    return {
        'form': OrderForm()
    }
