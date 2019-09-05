from django.contrib.syndication.views import Feed
from django.views.generic import View
from django.utils import feedgenerator

from sitesutils.helpers import get_site
from publications.models import MultisiteMixin, DatesMixin


class PublicationFeed(View, Feed):

    model = None
    feed_type = feedgenerator.Rss201rev2Feed

    def link(self):
        return get_site(self.request).domain

    def items(self):
        queryset = self.model.objects.published()
        if issubclass(self.model, MultisiteMixin):
            site = get_site(self.request)
            queryset = queryset.for_site(site)
        if issubclass(self.model, DatesMixin):
            queryset = queryset.order_by('-published_at')
        else:
            queryset = queryset.order_by('-created_at')
        return queryset[:10]

    def item_pubdate(self, item):
        if issubclass(self.model, DatesMixin):
            return item.published_at
        return item.created_at

    def get(self, request, *args, **kwargs):
        return self(request, *args, **kwargs)
