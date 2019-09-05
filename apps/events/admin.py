import lemon

from .models import Event, Transfer, EventOrder


class TrasferInline(lemon.StackedInline):

    model = Transfer
    extra = 1


class EventAdmin(lemon.ModelAdmin):

    list_display = ['title', 'event_date', 'date_start', 'date_stop', 'is_active']
    list_editable = ['is_active']
    markup_fields = ['description']
    inlines = [TrasferInline]
    tabs = True


class EventOrderAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'company', 'brend', 'created_at']
    list_filter = ['event']


lemon.site.register(Event, EventAdmin)
lemon.site.register(EventOrder, EventOrderAdmin)
