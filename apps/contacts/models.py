# coding: utf-8
from django.db import models


class Category(models.Model):

    title = models.CharField(u'категория', max_length=255)
    contacts = models.TextField(u'общие контакты', blank=True, null=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'категория контактов'
        verbose_name_plural = u'категории контактов'
        ordering = ['weight', 'pk']


class SubCategory(models.Model):

    title = models.CharField(u'категория', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'подкатегория контактов'
        verbose_name_plural = u'подкатегории контактов'
        ordering = ['weight', 'pk']


class Person(models.Model):

    category = models.ForeignKey(Category, verbose_name=u'категория')
    subcategory = models.ForeignKey(SubCategory, verbose_name=u'подкатегория', null=True, blank=True)
    position = models.CharField(u'должность', max_length=255)
    full_name = models.CharField(u'ФИО', max_length=255)
    phones = models.CharField(u'телефоны', max_length=255)
    email = models.CharField(u'email', max_length=255, blank=True)
    email2 = models.CharField(u'email 2', max_length=255, blank=True)
    email3 = models.CharField(u'email 3', max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'контактное лицо'
        verbose_name_plural = u'контакты'
        ordering = ['category', 'subcategory', 'weight', 'pk']


class Office(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'изображение', upload_to='contacts')
    text = models.TextField(u'контактная информация')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'представительство'
        verbose_name_plural = u'представительства'
        ordering = ['weight']


class Feedback(models.Model):

    full_name = models.CharField(u'имя', max_length=255)
    phone = models.CharField(u'телефон', max_length=255, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'сообщение')
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'сообщение обратной связи'
        verbose_name_plural = u'обратная связь'
        ordering = ['-created_at']
