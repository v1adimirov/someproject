from django.template import Library

from contacts.models import Office
from contacts.forms import FeedbackForm


register = Library()


@register.inclusion_tag('contacts/tags/office_list.html')
def office_list():
    return {'object_list': Office.objects.all()}


@register.inclusion_tag('contacts/feedback_form.html')
def feedback_form():
    return {'form': FeedbackForm()}
