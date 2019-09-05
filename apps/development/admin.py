# coding: utf-8
import lemon

from .models import DevelpmentPage, Icon, Direction, Asset, Link, OrderObject, OrderCity, Order, Variant


class IconInline(lemon.StackedInline):

    model = Icon
    extra = 3


class DirectionInline(lemon.StackedInline):

    model = Direction
    extra = 3


class AssetInline(lemon.StackedInline):

    model = Asset
    extra = 3


class LinkInline(lemon.StackedInline):

    model = Link
    extra = 3

class VariantInline(lemon.StackedInline):

    model = Variant
    extra = 1


class DevelpmentPageAdmin(lemon.ModelAdmin):

    inlines = [
        IconInline, DirectionInline, AssetInline, LinkInline, VariantInline
    ]
    tabs = True
    markup_fields = ['about_text', 'text2', 'contacts', 'text_var']


class OrderAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'phone', 'email', 'created_at']
    list_filter = ['obj', 'city']


lemon.site.register(DevelpmentPage, DevelpmentPageAdmin)
lemon.site.register(Order, OrderAdmin)
lemon.site.register(OrderCity)
lemon.site.register(OrderObject)
