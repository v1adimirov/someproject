from django.template import Library

from reviews.models import VideoReview, Review


register = Library()


@register.inclusion_tag('reviews/tags/video_reviews.html')
def video_reviews(city=None):
    qs = VideoReview.objects.filter(is_active=True)
    if city is not None:
        qs = qs.filter(city=city, on_act=True)
    else:
        qs = qs.filter(on_main=True)
    return {'object_list': qs}


@register.inclusion_tag('reviews/tags/reviews.html')
def reviews(city=None):
    qs = Review.objects.filter(is_active=True)
    if city is not None:
        qs = qs.filter(city=city, on_act=True).order_by('?')[:2]
    else:
        qs = qs.filter(on_main=True).order_by('?')[:2]
    return {'object_list': qs}
