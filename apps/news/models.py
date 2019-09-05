# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


CATGORIES = (
    ('news', u'Новости'),
    ('press', u'СМИ о нас')
)


class NewsItem(models.Model):

    category = models.CharField(u'категория', max_length=50, choices=CATGORIES)
    title = models.CharField(u'заголовок', max_length=255)
    image = models.ImageField(u'главное изображение', upload_to='news', null=True)
    preview = models.TextField(u'анонс')
    content = models.TextField(u'текст новости')
    publication_date = models.DateField(u'дата публикации')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('news_newsitem_detail', args=[self.category, self.pk])

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-publication_date', '-created_at']


class NewsItemImage(models.Model):

    newsitem = models.ForeignKey(NewsItem, related_name='images')
    image = models.ImageField(u'изображение', upload_to='news')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'изображением'
        verbose_name_plural = u'изображения'
        ordering = ['weight', 'pk']
