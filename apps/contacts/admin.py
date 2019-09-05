import lemon

from .models import Category, SubCategory, Person, Office


class CategoryAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight']
    list_editable = ['weight']
    markup_fields = ['contacts']


class SubCategoryAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight']
    list_editable = ['weight']


class PersonAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'category', 'subcategory', 'weight', 'is_active']
    list_editable = ['is_active', 'weight']
    list_filter = ['category', 'subcategory']
    search_fields = ['full_name', 'email', 'email2', 'email3']


class OfficeAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight']
    list_editable = ['weight']


lemon.site.register(Category, CategoryAdmin)
lemon.site.register(SubCategory, SubCategoryAdmin)
lemon.site.register(Person, PersonAdmin)
lemon.site.register(Office, OfficeAdmin)
