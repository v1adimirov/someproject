# coding: utf-8
from haystack import indexes

from .models import Contacts


class SearchIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Contacts

    def prepare_title(self, object):
        return u'Аренда'

    def prepare_absolute_url(self, object):
        return '/lease/'
