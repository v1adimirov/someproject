# coding: utf-8
from haystack import indexes

from .models import (
    City, Location, Concept, VologdaCity, VologdaMart,
    PhotoReport, FranchCity, FranchVologda
)


class CityIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return City

    def prepare_title(self, object):
        return unicode(object.title)

    def prepare_absolute_url(self, object):
        return object.get_absolute_url()


class LocationIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Location

    def prepare_title(self, object):
        return unicode(object.city.title)

    def prepare_absolute_url(self, object):
        return object.city.get_absolute_url()


class ConceptIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return Concept

    def prepare_title(self, object):
        return unicode(object.city.title)

    def prepare_absolute_url(self, object):
        return object.city.get_absolute_url()


class VologdaCityIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return VologdaCity

    def prepare_title(self, object):
        return u'Вологда'

    def prepare_absolute_url(self, object):
        return '/region/vologda/'


class VologdaMartIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return VologdaMart

    def prepare_title(self, object):
        return unicode(object.title)

    def prepare_absolute_url(self, object):
        return '/region/vologda/'


# class PhotoReportIndex(indexes.SearchIndex, indexes.Indexable):

#     title = indexes.CharField()
#     text = indexes.CharField(document=True, use_template=True)
#     absolute_url = indexes.CharField()

#     def get_model(self):
#         return PhotoReport

#     def prepare_title(self, object):
#         return u'Фотоотчет' + unicode(object.city.title) + unicode(object.title)

#     def prepare_absolute_url(self, object):
#         return object.get_absolute_url()


class FranchCityIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return FranchCity

    def prepare_title(self, object):
        return  u'Франчайзинг' + unicode(object.city.title)

    def prepare_absolute_url(self, object):
        return object.get_absolute_url()


class FranchVolodaIndex(indexes.SearchIndex, indexes.Indexable):

    title = indexes.CharField()
    text = indexes.CharField(document=True, use_template=True)
    absolute_url = indexes.CharField()

    def get_model(self):
        return FranchVologda

    def prepare_title(self, object):
        return  u'Франчайзинг' + unicode(object.mart.title)

    def prepare_absolute_url(self, object):
        return object.get_absolute_url()
