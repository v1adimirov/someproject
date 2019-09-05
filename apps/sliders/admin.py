import lemon

from sliders.models import MainSliderItem


class MainSliderItemAdmin(lemon.ModelAdmin):

    list_display = ['__unicode__', 'weight', 'is_active']
    list_editable = ['weight', 'is_active']
    list_filter = ['is_active']
    markup_fields = ['text']


lemon.site.register(MainSliderItem, MainSliderItemAdmin)
