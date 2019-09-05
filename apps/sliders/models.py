# coding: utf-8
from django.db import models


class MainSliderItem(models.Model):

    image = models.ImageField(u'изображение', upload_to='sliders')
    link = models.CharField(u'ссылка', max_length=500, blank=True)
    title = models.CharField(u'заголовок', max_length=255, blank=True)
    subtitle = models.CharField(u'подзаголовок', max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def __unicode__(self):
        return self.title or self.subtitle or self.image.url

    class Meta:
        verbose_name = u'элемент слайдера'
        verbose_name_plural = u'слайдер на главной странице'
        ordering = ['weight', 'pk']
