# coding: utf-8
from django.db import models


ASSETS_ICONS = (
    ('_1', u'строим'),
    ('_2', u'инвестируем'),
    ('_3', u'управляем'),
)

DIRECTION_ICONS = (
    ('_development', u'девелопмент недвижимости'),
    ('_retail', u'ритейл'),
    ('_distribution', u'дистрибьюция')
)


class DevelpmentPage(models.Model):

    about_title = models.CharField(u'заголовок "о компании"', max_length=255)
    about_text = models.TextField(u'Текст о компании')
    text2 = models.TextField(u'текст 2')
    text_var = models.TextField(u'Текст "варианты сотрудничества"', blank=True, default="")
    contacts = models.TextField('контакты')

    def __unicode__(self):
        return u'Страница Развитие'

    class Meta:
        verbose_name = u'Страница Развитие'
        verbose_name_plural = u'Страница Развитие'


class Icon(models.Model):

    page = models.ForeignKey(DevelpmentPage, related_name='icons')
    icon = models.CharField(u'иконка', choices=ASSETS_ICONS, max_length=50)
    title = models.CharField(u'заголовок', max_length=500)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'иконка'
        verbose_name_plural = u'иконки'
        ordering = ['weight', 'pk']


class Direction(models.Model):

    page = models.ForeignKey(DevelpmentPage, related_name='directions')
    icon = models.CharField(u'иконка', choices=DIRECTION_ICONS, max_length=50)
    title = models.CharField(u'заголовок', max_length=255)
    link = models.CharField(u'ссылка', max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'направление'
        verbose_name_plural = u'направления'
        ordering = ['weight', 'pk']

class Variant(models.Model):

    page = models.ForeignKey(DevelpmentPage, related_name='variants')
    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'иконка', upload_to='development')
    link = models.CharField(u'ссылка', max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'вариант'
        verbose_name_plural = u'варианты сотрудничества'
        ordering = ['weight', 'pk']


class Asset(models.Model):

    page = models.ForeignKey(DevelpmentPage, related_name='assets')
    image = models.ImageField(u'изображения', upload_to='development')
    year = models.CharField(u'год', max_length=10)
    addr = models.TextField(u'адрес')
    props = models.TextField(u'параметры')
    link = models.CharField(u'ссылка', max_length=255, null=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.year

    class Meta:
        verbose_name = u'объекты'
        verbose_name_plural = u'объекты'
        ordering = ['weight', 'pk']


class Link(models.Model):

    page = models.ForeignKey(DevelpmentPage, related_name='links')
    title = models.CharField(u'заголовок', max_length=255)
    link = models.CharField(u'ссылка', max_length=255, blank=True)
    text = models.TextField(u'Текст')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'сслыка'
        verbose_name_plural = u'ссылки'
        ordering = ['weight', 'pk']


class OrderObject(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    weight = models.PositiveIntegerField(default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'объект в заявке'
        verbose_name_plural = u'объекты в заявке'
        ordering = ['weight', 'pk']


class OrderCity(models.Model):
    title = models.CharField(u'заголовок', max_length=255)
    weight = models.PositiveIntegerField(default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'город в заявке'
        verbose_name_plural = u'города в заявке'
        ordering = ['weight', 'pk']


class Order(models.Model):

    obj = models.ForeignKey(OrderObject, verbose_name='объект', null=True, blank=True)
    area = models.CharField(u'площадь', max_length=255)
    city = models.ForeignKey(OrderCity, verbose_name='город', null=True, blank=True)
    address = models.CharField(u'адрес', max_length=255)
    full_name = models.CharField(u'ФИО', max_length=255)
    phone = models.CharField(u'телефон', max_length=255)
    email = models.EmailField(u'email', max_length=255)
    text = models.TextField(u'сообщение', blank=True, null=True)
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'заявка в развитии'
        verbose_name_plural = u'заявки в развитии'
        ordering = ['-created_at']
