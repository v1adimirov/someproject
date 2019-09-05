# coding: utf-8
from haystack import indexes

from .models import (
    SaleObject
)


class SaleObjectIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return SaleObject

    def prepare_title(self, object):
        return unicode(object.title)

    def prepare_absolute_url(self, object):
        return object.get_absolute_url()
