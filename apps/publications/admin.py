from django.utils.translation import ugettext_lazy as _

import lemon as admin
from publications.models import MultisiteMixin, MultilingualMixin, DatesMixin, WeightMixin


class PublicationAdmin(admin.ModelAdmin):
    """Default configuration for admin publications."""

    actions = ['make_enabled', 'make_disabled']
    list_per_page = 25

    extend_fieldsets = True
    extend_list_filter = True
    extend_list_display = True

    def __init__(self, *args, **kwargs):
        super(PublicationAdmin, self).__init__(*args, **kwargs)
        if issubclass(self.model, WeightMixin) and not self.list_editable:
            self.list_editable = ['weight']
        if issubclass(self.model, DatesMixin) and not self.date_hierarchy:
            self.date_hierarchy = 'published_at'

    def make_enabled(self, request, queryset):
        """Action which set enabled field to True."""
        queryset.update(enabled=True)
    make_enabled.short_description = _('Enable selected %(verbose_name_plural)s')

    def make_disabled(self, request, queryset):
        """Action which set enabled field to False."""
        queryset.update(enabled=False)
    make_disabled.short_description = _('Disable selected %(verbose_name_plural)s')

    def get_ordering(self, request):
        if self.ordering:
            return self.ordering
        if issubclass(self.model, WeightMixin):
            return ['weight']
        if issubclass(self.model, DatesMixin):
            return ['-published_at']
        return ()

    def get_list_display(self, request):
        list_display = super(PublicationAdmin, self).get_list_display(request)
        if self.extend_list_display:
            list_display = (
                list(list_display) +
                list(self.get_publication_list_display(request))
            )
        return list_display

    def get_publication_list_display(self, request):
        list_display = ['enabled']
        if issubclass(self.model, WeightMixin):
            list_display.append('weight')
        if issubclass(self.model, DatesMixin):
            list_display.insert(0, 'published_at')
        if issubclass(self.model, MultilingualMixin):
            list_display.insert(0, 'language')
        return list_display

    def get_fields(self, request, obj=None):
        if self.fields:
            return self.fields
        fields = super(PublicationAdmin, self).get_fields(request, obj)
        publication_fields = self.get_publication_fields(request, obj)
        return [field for field in fields if field not in publication_fields]

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(PublicationAdmin, self).get_fieldsets(request, obj)
        if self.extend_fieldsets:
            fieldsets += self.get_publication_fieldsets(request, obj)
        return fieldsets

    def get_publication_fields(self, request, obj=None):
        fields = ['enabled']
        if issubclass(self.model, DatesMixin):
            fields.append('published_at')
            fields.append('expires_at')
        if issubclass(self.model, WeightMixin):
            fields.insert(0, 'weight')
        if issubclass(self.model, MultisiteMixin):
            fields.insert(0, 'sites')
        if issubclass(self.model, MultilingualMixin):
            fields.insert(0, 'language')
        return fields

    def get_publication_fieldsets(self, request, obj=None):
        return (
            (_('Publication parameters'), {
                'classes': ('wide',),
                'fields': self.get_publication_fields(request, obj),
            }),
        )

    def get_list_filter(self, request):
        list_filter = super(PublicationAdmin, self).get_list_filter(request)
        if self.extend_list_filter:
            list_filter = (
                list(list_filter) +
                list(self.get_publication_list_filter(request))
            )
        return list_filter

    def get_publication_list_filter(self, request):
        list_filter = ['enabled', 'created_at', 'updated_at']
        if issubclass(self.model, DatesMixin):
            list_filter.insert(1, 'published_at')
        if issubclass(self.model, MultisiteMixin):
            list_filter.insert(0, 'sites')
        if issubclass(self.model, MultilingualMixin):
            list_filter.insert(0, 'language')
        return list_filter
