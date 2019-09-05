# coding: utf-8
import requests
import re
from StringIO import StringIO
from django.core.files import File
from django.db import models

from assets.models import City


class VideoReview(models.Model):

    city = models.ForeignKey(City, related_name='videoreviews', null=True, blank=True)
    title = models.CharField(u'название', max_length=255)
    video_link = models.CharField(u'ссылка на видео', max_length=255)
    video_image = models.ImageField(u'превью видеоролика', upload_to='reviews', null=True, blank=True)
    on_main = models.BooleanField(u'на главной', default=False)
    on_act = models.BooleanField(u'на странице торгового центра', default=False)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def _get_youtube_id(self):
        match = re.search(r'youtube.com/watch\?v=([\w\d-]+)$', self.video_link)
        if match:
            return match.group(1)
        else:
            match = re.search(r'youtu\.be/([^&#]+)[#&]{0,1}.{0,}$', self.video_link)
            if match:
                return match.group(1)
            else:
                match = re.search(r'youtube.com/embed/([\w\d-]+)$', self.video_link)
                if match:
                    return match.group(1)
                else:
                    match = re.search(r'youtube.com/embed/([\w\d-]+)$', self.video_link)
                    if match:
                        return match.group(1)
        return 'VQ2J2G0eMDk' # рандомный ID на всякий случай

    def get_video_url(self):
        youtibe_id = self._get_youtube_id()
        return 'http://www.youtube.com/embed/{}'.format(youtibe_id)

    def get_preview_url(self):
        youtibe_id = self._get_youtube_id()
        return 'http://img.youtube.com/vi/{}/0.jpg'.format(youtibe_id)

    @property
    def video_preview(self):
        if not self.video_image:
            r = requests.get(self.get_preview_url())
            if r.status_code == 200:
                image_data = StringIO(r.content)
                self.video_image.save('{}_preview.jpg'.format(self.pk), File(image_data))
                self.save()
        return self.video_image

    def resave_video_preview(self):
        r = requests.get(self.get_preview_url())
        if r.status_code == 200:
            image_data = StringIO(r.content)
            self.video_image.save('{}_preview.jpg'.format(self.pk), File(image_data))
            self.save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'видео отзыв'
        verbose_name_plural = u'видео отзывы'
        ordering = ['weight', 'pk']


class Review(models.Model):

    city = models.ForeignKey(City, related_name='reviews', null=True, blank=True)
    title = models.CharField(u'от кого', max_length=255)
    image = models.ImageField(u'изображение', upload_to='reviews')
    text = models.TextField(u'текст отзыва')
    on_main = models.BooleanField(u'на главной', default=False)
    on_act = models.BooleanField(u'на странице торгового центра', default=False)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'отзыв'
        verbose_name_plural = u'отзывы'
        ordering = ['weight', 'pk']
