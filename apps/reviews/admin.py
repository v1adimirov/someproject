import lemon

from .models import VideoReview, Review


class VideoReviewAdmin(lemon.ModelAdmin):

    list_display = ['title', 'city', 'on_main', 'on_act', 'is_active', 'weight']
    list_editable = ['on_main', 'on_act', 'is_active', 'weight']
    list_filter = ['city', 'on_main', 'on_act', 'is_active']


class ReviewAdmin(lemon.ModelAdmin):

    list_display = ['title', 'city', 'on_main', 'on_act', 'is_active', 'weight']
    list_editable = ['on_main', 'on_act', 'is_active', 'weight']
    list_filter = ['city', 'on_main', 'on_act', 'is_active']
    markup_fields = ['text']


lemon.site.register(VideoReview, VideoReviewAdmin)
lemon.site.register(Review, ReviewAdmin)
