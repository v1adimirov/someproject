# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class SaleObject(models.Model):

    title = models.CharField(u'название', max_length=255)
    address = models.CharField(u'адрес', max_length=255)
    image = models.ImageField(u'изображение', upload_to='sale')
    preview = models.TextField(u'краткое описание')
    content = models.TextField(u'описание')
    type = models.CharField(u'тип', max_length=255)
    area = models.CharField(u'земельный участок, кв.м.', max_length=50)
    gba = models.CharField(u'GBA кв.м.', max_length=50)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def get_absolute_url(self):
        return reverse('sale_saleobject_detail', args=[self.pk])

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'объект на продажу'
        verbose_name_plural = u'объекты на продажу'
        ordering = ['weight', 'pk']


class SaleProperty(models.Model):

    sale = models.ForeignKey(SaleObject, related_name='properties')
    title = models.CharField(u'название', max_length=255)
    value = models.CharField(u'значение', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = 'свойство'
        verbose_name_plural = u'прочие свойства'
        ordering = ['weight', 'pk']


class SaleImage(models.Model):

    sale = models.ForeignKey(SaleObject, related_name='images')
    image = models.ImageField(u'изображение', upload_to='sale')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = u'изображения'
        ordering = ['weight', 'pk']


class Contacts(models.Model):

    full_name = models.CharField(u'ФИО специалиста', max_length=255)
    position = models.CharField(u'должность', max_length=255)
    phones = models.CharField(u'телефоны', max_length=255)
    email = models.EmailField(u'email', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'сотрудник'
        verbose_name_plural = u'Сотрудники по продаже'
        ordering = ['weight', 'pk']
