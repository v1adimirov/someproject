from django.template import Library

from assets.models import City, VologdaMart, VologdaCity
from assets.forms import (
    FeedbackForm, VologdaFeedbackForm,
    FranchCityFeedbackForm, FranchVologdaFeedbackForm,
    MartFeedbackForm, FranchMartFeedbackForm
)


register = Library()


@register.inclusion_tag('assets/tags/city_list.html')
def assets_list():
    return {'object_list': City.objects.filter(is_active=True)}


@register.inclusion_tag('assets/feedback_form.html')
def feedback_form():
    return {
        'form': FeedbackForm()
    }


@register.inclusion_tag('assets/vologdafeedback_form.html')
def vologda_feedback_form():
    return {
        'form': VologdaFeedbackForm()
    }


@register.inclusion_tag('assets/martfeedback_form.html')
def mart_feedback_form():
    return {
        'form': MartFeedbackForm()
    }


@register.inclusion_tag('assets/franchcityfeedback_form.html')
def franchcity_feedback_form():
    return {
        'form': FranchCityFeedbackForm()
    }


@register.inclusion_tag('assets/franchvologdafeedback_form.html')
def franchvologda_feedback_form():
    return {
        'form': FranchVologdaFeedbackForm()
    }


@register.inclusion_tag('assets/franchmartfeedback_form.html')
def franchmart_feedback_form():
    return {
        'form': FranchMartFeedbackForm()
    }

@register.inclusion_tag('assets/tags/assets_menu.html')
def assets_menu():
    return {'object_list': City.objects.filter(is_active=True)}


@register.inclusion_tag('assets/tags/mart_list.html')
def vologda_mart_list():
    return {'object_list': VologdaMart.objects.all()}


@register.inclusion_tag('assets/tags/mark_list.html')
def city_mark_list(city):
    return {'object_list': city.marts.all()}


@register.inclusion_tag('assets/tags/vologda_item.html')
def vologda_item():
    try:
        obj = VologdaCity.objects.all()[0]
    except IndexError:
        obj = None
    return {'object': obj}


@register.inclusion_tag('assets/tags/mark_list.html')
def vologda_mark_list():
    return {'object_list': VologdaMart.objects.all()}


@register.inclusion_tag('assets/tags/interactive_map.html')
def interactive_map():
    qs = City.objects.filter(is_active=True)
    city_links = {}
    for obj in qs:
        city_links[obj.slug] = obj.get_absolute_url()
    return {'city_links': city_links}


@register.inclusion_tag('assets/tags/index_geo.html')
def assets_index_geo():
    qs = City.objects.filter(is_active=True)
    city_links = {}
    for obj in qs:
        city_links[obj.slug] = obj.get_absolute_url()
    return {'city_links': city_links, 'STATIC_URL': '/static/'}
