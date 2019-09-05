import lemon

from .models import Order, Mart, Contacts, ContactsEmail


class MartAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight', 'is_active']
    list_editable = ['weight', 'is_active']


class OrderAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'mart', 'company', 'whence', 'created_at']
    list_filter = ['mart']


class ContactsEmailInline(lemon.StackedInline):

    model = ContactsEmail
    extra = 1


class ContactsAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'is_new', 'is_old', 'weight']
    list_editable = ['is_new', 'is_old', 'weight']
    list_filter = ['is_new', 'is_old']
    inlines = [ContactsEmailInline]


lemon.site.register(Mart, MartAdmin)
lemon.site.register(Order, OrderAdmin)
lemon.site.register(Contacts, ContactsAdmin)
