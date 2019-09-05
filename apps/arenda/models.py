# coding: utf-8
from django.db import models
from django.conf import settings


class Mart(models.Model):

    title = models.CharField(u'название', max_length=255)
    arenda_type = models.PositiveIntegerField(
        u'Тип объекта для заявки на аренду',
        choices=settings.ARENDA_TYPES,
        default=1, blank=True, null=True
    )
    image = models.ImageField(u'изображение', null=True, blank=True, upload_to='arenda')
    link = models.CharField(u'ссылка на страницу ТЦ', max_length=255, null=True, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'торговый центр'
        verbose_name_plural = u'торговые центры'
        ordering = ['weight', 'pk']


class Order(models.Model):

    area = models.CharField(u'площадь', max_length=255)
    mart = models.ForeignKey(Mart, verbose_name=u'торговый центр', null=True)
    products = models.CharField(u'категория товаров', max_length=255, blank=True)
    comment = models.TextField(u'комментраий', blank=True)
    full_name = models.CharField(u'ФИО', max_length=255)
    phone = models.CharField(u'телефон', max_length=255, blank=True)
    email = models.EmailField(u'Email', max_length=255)
    trademark = models.CharField(u'торговая марка', max_length=255, blank=True)
    company = models.CharField(u'компания', max_length=255, blank=True)
    whence = models.CharField(u'откуда вы узнали о ТРЦ', max_length=255, blank=True)
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'заявка'
        verbose_name_plural = u'заявки'
        ordering = ['-created_at']


class Contacts(models.Model):

    full_name = models.CharField(u'ФИО специалиста', max_length=255)
    is_new = models.BooleanField(u'аренда в строящихся', default=False)
    is_old = models.BooleanField(u'аренда в действующих', default=False)
    position = models.CharField(u'должность', max_length=255)
    phones = models.CharField(u'телефоны', max_length=255)
    cities = models.CharField(u'города', max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'специалист'
        verbose_name_plural = u'контактные данные специалистов'
        ordering = ['weight', 'pk']


class ContactsEmail(models.Model):

    contacts = models.ForeignKey(Contacts, related_name='emails')
    email = models.EmailField(u'email', max_length=255)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'email'
        verbose_name_plural = u'email'
