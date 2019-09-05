# coding: utf-8
from django.db import models


class Event(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    event_date = models.DateField(u'дата мероприятия')
    description = models.TextField(u'описание')
    date_start = models.DateTimeField(u'дата начала приема заявок')
    date_stop = models.DateTimeField(u'дата окончания приема заявок')
    program = models.FileField(u'программа мероприятия', upload_to='events', null=True, blank=True)
    is_active = models.BooleanField(u'активное', default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'мероприятие'
        verbose_name_plural = u'мероприятия'
        ordering = ['-date_start', '-date_stop']


class Transfer(models.Model):

    event = models.ForeignKey(Event, verbose_name=u'мероприятие', related_name='transfers')
    title = models.CharField(u'заголовок', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'вариант'
        verbose_name = u'варианты проезда'
        ordering = ['weight', 'pk']


class EventOrder(models.Model):

    event = models.ForeignKey(Event, verbose_name=u'мероприятие', related_name='orders')
    full_name = models.CharField(u'ФИО', max_length=255)
    company = models.CharField(u'название компании', max_length=255)
    brend = models.CharField(u'Бренд', max_length=255, null=True)
    city = models.CharField(u'город', max_length=255)
    phone = models.CharField(u'телефон', max_length=255)
    email = models.EmailField(u'email', max_length=255)
    transfer = models.ForeignKey(Transfer, verbose_name=u'способ доставки', null=True, blank=True)
    message = models.TextField(u'сообщение', blank=True)
    ip = models.CharField(u'IP', max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = u'заявка на мероприятие'
        verbose_name_plural = u'заявки на мероприятие'
        ordering = ['-created_at']
