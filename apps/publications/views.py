from django.views.generic import (
    ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView,
    WeekArchiveView, DayArchiveView, TodayArchiveView, DateDetailView,
)
from sitesutils.helpers import get_site
from publications.models import MultisiteMixin, MultilingualMixin, DatesMixin, WeightMixin


class PublicationMixin(object):

    date_field = 'published_at'

    def get_queryset(self):
        queryset = super(PublicationMixin, self).get_queryset()
        if issubclass(queryset.model, MultisiteMixin):
            site = get_site(self.request)
            queryset = queryset.for_site(site)
        if issubclass(queryset.model, MultilingualMixin):
            queryset = queryset.in_language()
        if issubclass(queryset.model, WeightMixin):
            queryset = queryset.order_by('weight')
        elif issubclass(queryset.model, DatesMixin):
            queryset = queryset.order_by('-published_at')
        return queryset.published()


class PublicationListView(PublicationMixin, ListView):
    """Works like ListView but returns only published objects."""


class PublicationDetailView(PublicationMixin, DetailView):
    """Works like DetailView but returns object only if published."""


class PublicationArchiveIndexView(PublicationMixin, ArchiveIndexView):
    """Works like ArchiveIndexView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationYearArchiveView(PublicationMixin, YearArchiveView):
    """Works like YearArchiveView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationMonthArchiveView(PublicationMixin, MonthArchiveView):
    """Works like MonthArchiveView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationWeekArchiveView(PublicationMixin, WeekArchiveView):
    """Works like WeekArchiveView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationDayArchiveView(PublicationMixin, DayArchiveView):
    """Works like DayArchiveView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationTodayArchiveView(PublicationMixin, TodayArchiveView):
    """Works like TodayArchiveView but returns only published objects and uses
    published_at as date_field.
    """


class PublicationDateDetailView(PublicationMixin, DateDetailView):
    """Works like DateDetailView but returns object only if published and uses
    published_at as date_field.
    """
