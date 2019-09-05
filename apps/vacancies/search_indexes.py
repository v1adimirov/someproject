# coding: utf-8
from haystack import indexes

from .models import (
    Vacancy
)


class SaleObjectIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Vacancy

    def prepare_title(self, object):
        return u'Вакансия' + unicode(object.position)

    def prepare_absolute_url(self, object):
        return '/vacancy/'
