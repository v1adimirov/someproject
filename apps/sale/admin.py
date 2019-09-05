import lemon

from .models import SaleObject, SaleProperty, SaleImage, Contacts


class SalePropertyInline(lemon.StackedInline):

    model = SaleProperty
    extra = 1


class SaleImageInline(lemon.StackedInline):

    model = SaleImage
    extra = 3


class SaleObjectAdmin(lemon.ModelAdmin):

    list_display = ['title', 'address', 'weight']
    list_editable = ['weight']
    markup_fields = ['preview', 'content']
    inlines = [SalePropertyInline, SaleImageInline]
    tabs = True


lemon.site.register(SaleObject, SaleObjectAdmin)

lemon.site.register(Contacts)
