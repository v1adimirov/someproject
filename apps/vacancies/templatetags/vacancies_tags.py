from django.template import Library

from vacancies.models import ContactPerson


register = Library()


@register.inclusion_tag('vacancies/tags/contact_list.html')
def vacancies_contacts():
    return {'object_list': ContactPerson.objects.all()}
