# coding: utf-8
from haystack import indexes

from .models import (
    Category, SubCategory, Person
)


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Category

    def prepare_title(self, object):
        return u'Контакты'

    def prepare_absolute_url(self, object):
        return '/contacts/'


class SubCategoryIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return SubCategory

    def prepare_title(self, object):
        return u'Контакты'

    def prepare_absolute_url(self, object):
        return '/contacts/'


class PersonIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Person

    def prepare_title(self, object):
        return u'Контакты'

    def prepare_absolute_url(self, object):
        return '/contacts/'