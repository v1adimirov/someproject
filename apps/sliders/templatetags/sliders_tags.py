from django.template import Library

from sliders.models import MainSliderItem


register = Library()


@register.inclusion_tag('sliders/tags/main_slider.html')
def main_slider():
    return {'object_list': MainSliderItem.objects.filter(is_active=True)}
