# coding: utf-8
import re
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import QuerySet


class City(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    title_2 = models.CharField(u'заголовок для списка ТЦ и ТРЦ', max_length=255, blank=True, null=True)
    city = models.CharField(u'город', max_length=255)
    slug = models.CharField(u'slug', max_length=255, unique=True)
    image = models.ImageField(u'изображение', upload_to='assert', null=True)
    preview_image = models.ImageField(u'изображение списка', upload_to='assert', null=True)
    preview_image_2 = models.ImageField(u'изображение списка ТЦ и ТРЦ', upload_to='assert', null=True, blank=True)
    area = models.CharField(u'площадь', max_length=255, null=True)
    address = models.CharField(u'адрес', max_length=255, null=True)
    peview = models.TextField(u'тест в списке')
    peview_2 = models.TextField(u'тест в списке ТЦ и ТРЦ', blank=True, null=True)
    text = models.TextField(u'текстовый блок 1')
    text2 = models.TextField(u'текстовый блок 2', blank=True)
    text3 = models.TextField(u'текстовый блок 3', blank=True)
    text4 = models.TextField(u'текстовый блок 4', blank=True)
    text5 = models.TextField(u'текстовый блок 5', blank=True)
    list_text = models.TextField(u'текст в списке с другими ТЦ (если есть)', blank=True)
    phone = models.CharField(u'телефон', max_length=255)
    email = models.EmailField(u'email', max_length=255, blank=True)
    contact_person = models.CharField(u'контактное лицо', max_length=255)
    contact_photo = models.ImageField(u'фото контактного лица', upload_to='assert', blank=True, null=True)

    phone2 = models.CharField(u'телефон 2', max_length=255, blank=True, null=True)
    email2 = models.EmailField(u'email 2', max_length=255, blank=True, null=True)
    contact_person2 = models.CharField(u'контактное лицо 2', max_length=255, blank=True, null=True)
    contact_photo2 = models.ImageField(u'фото контактного лица 2', upload_to='assert', blank=True, null=True)

    recipient_email = models.EmailField(u'email для вопросов', max_length=255, blank=True)
    city_recipient_email = models.EmailField(u'email для вопросов общий для города (в случае нескльких ТЦ)', max_length=255, blank=True)
    video_title = models.CharField(u'заголовок видео', max_length=255, blank=True)
    video_link = models.CharField(u'ссылка на YouTube', max_length=255, blank=True)
    video_text = models.TextField(u'тест под видео', blank=True)
    site = models.CharField(u'ссылка на сайт ТРЦ', max_length=255, blank=True, null=True)
    franch_text = models.TextField(u'Текст на странице с франшизами', blank=True, null=True)
    online_video = models.CharField(u'онлайн трансляция строительства', max_length=255, blank=True)
    presentation = models.FileField(u'презентация проекта', upload_to='assets', null=True, blank=True)
    vk_link = models.CharField(u'ссылка ВКонтакте', max_length=255, blank=True)
    fb_link = models.CharField(u'ссылка Facebook', max_length=255, blank=True)
    yt_link = models.CharField(u'ссылка YouTube', max_length=255, blank=True)
    ig_link = models.CharField(u'ссылка Instagram', max_length=255, blank=True)
    map_latitude = models.CharField(u'широта центра карты', max_length=255)
    map_longitude = models.CharField(u'долгота центра карты', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    metrica_target = models.CharField(u'цель Я.Метрики для заявки', max_length=255, null=True, blank=True)
    call_metrica_target = models.CharField(u'цель Я.Метрики для заказа звонка', max_length=255, null=True, blank=True)
    quetion_metrica_target = models.CharField(u'цель Я.Метрики для задать вопрос', max_length=255, null=True, blank=True)
    has_marts = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(u'активный', default=True)

    def get_video_url(self):
        match = re.search('^http://www.youtube.com/watch\?v=([\w\d-]+)$', self.video_link)
        if match:
            return 'http://www.youtube.com/embed/{}'.format(match.group(1))
        else:
            match = re.search(r'youtu\.be/([^&#]+)[#&]{0,1}.{0,}$', self.video_link)
            if match:
                return 'http://www.youtube.com/embed/{}'.format(match.group(1))
        return self.video_link

    def get_detail_url(self):
        return reverse('assets_city_detail', args=[self.slug])

    def get_absolute_url(self):
        if self.has_marts:
            return reverse('assets_city_marts_list', args=[self.slug])
        return self.get_detail_url()

    def has_actual_info(self):
        return self.has_photoreport() or self.has_online_video() or self.presentation or self.vk_link or self.yt_link or self.ig_link

    def has_photoreport(self):
        return self.photoreport_set.all().exists()

    def has_online_video(self):
        return self.cameras.all().exists()

    def __unicode__(self):
        return self.city

    class Meta:
        verbose_name = u'город'
        verbose_name_plural = u'активы'
        ordering = ['weight', 'city']


class CityReward(models.Model):

    city = models.ForeignKey(City, related_name='rewards')
    image = models.ImageField(u'изображение', upload_to='assets')
    text = models.TextField(u'поисание награды')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'награда'
        verbose_name_plural = u'достижения'
        ordering = ['weight', 'pk']


class CityRecipientEmail(models.Model):

    city = models.ForeignKey(City, related_name='recipients')
    email = models.EmailField(u'email', max_length=255)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'получатель'
        verbose_name_plural = u'получатели'


MARK_TYPES = (
    ('default', u'Обычная'),
    ('MassTransitCircleIcon', u'Автобусная остановка'),
    ('VegetationCircleIcon', u'Парк'),
    ('default', u'Обычная'),
)


class MapMarkCoordsQuerySet(QuerySet):

    def marts(self):
        return self.filter(mark_type__isnull=True)

    def special_marks(self):
        return self.filter(mark_type__isnull=False)


class MapMarkCoords(models.Model):

    city = models.ForeignKey(City, related_name='marks')
    title = models.CharField(u'заголовок', max_length=255)
    latitude = models.CharField(u'широта', max_length=255)
    longitude = models.CharField(u'долгота', max_length=255)
    mark_type = models.CharField(
        u'тип метки', max_length=100,
        blank=True, null=True,
        help_text=u'оставте поле незаполненным если это метка ТЦ'
    )

    objects = MapMarkCoordsQuerySet.as_manager()

    class Meta:
        verbose_name = u'метка'
        verbose_name_plural = u'метки на карте'


class Partner(models.Model):

    city = models.ForeignKey(City, related_name='parthners')
    title = models.CharField(u'заголовок', max_length=255, null=True, blank=True)
    image = models.ImageField(u'изображение', upload_to='mainpage')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title or self.image.url

    class Meta:
        verbose_name = u'партнер'
        verbose_name_plural = u'партнеры'
        ordering = ['weight', 'pk']


class Number(models.Model):

    city = models.ForeignKey(City, related_name='numbers')
    number = models.CharField(u'цифра', max_length=255)
    note = models.CharField(u'подпись', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.note

    class Meta:
        verbose_name = u'цифра'
        verbose_name_plural = u'цифры'
        ordering = ['weight', 'pk']


class AssetImage(models.Model):

    city = models.ForeignKey(City, related_name='images')
    title = models.CharField(u'заголовок', max_length=255, blank=True)
    image = models.ImageField('изображение', upload_to='assets')

    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title or self.image.url

    class Meta:
        verbose_name = u'изображения'
        verbose_name_plural = u'изображение'
        ordering = ['weight', 'pk']


class Location(models.Model):

    city = models.ForeignKey(City, related_name='locations')
    text = models.TextField(u'тест')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'локация'
        verbose_name_plural = u'локация'
        ordering = ['weight', 'pk']


class Concept(models.Model):

    city = models.ForeignKey(City, related_name='concepts')
    text = models.TextField(u'тест')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'концепция'
        verbose_name_plural = u'концепция'
        ordering = ['weight', 'pk']


class Plan(models.Model):

    city = models.ForeignKey(City, related_name='plans')
    image = models.ImageField(u'изображение плана', upload_to='assets')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'план'
        verbose_name_plural = u'изображения плана'
        ordering = ['weight', 'pk']


class Feedback(models.Model):

    city = models.ForeignKey(City, verbose_name='город', null=True, blank=True)
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


class Camera(models.Model):

    city = models.ForeignKey(City, related_name='cameras')
    code = models.TextField(u'код камеры')

    class Meta:
        verbose_name = u'камера наблюдения'
        verbose_name_plural = u'камеры наблюдения'


class VologdaCity(models.Model):

    image = models.ImageField(u'изображение', upload_to='assets')
    preview = models.TextField(u'текст в списке')
    recipient_email = models.EmailField(u'Email получателя', max_length=255, default='kits@maxi-net.ru')
    text = models.TextField(u'текст')
    call_metrica_target = models.CharField(u'цель Я.Метрики для задать вопрос', max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u'Вологда'

    class Meta:
        verbose_name = u'Вологда'
        verbose_name_plural = u'Вологда'


class VologdaRecipientEmail(models.Model):

    city = models.ForeignKey(VologdaCity, related_name='recipients')
    email = models.EmailField(u'email', max_length=255)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'получатель'
        verbose_name_plural = u'получатели'


class VologdaMart(models.Model):

    title = models.CharField(u'загололок', max_length=255)
    image = models.ImageField(u'изображение', upload_to='assets')
    address = models.CharField(u'адрес', max_length=255)
    area = models.CharField(u'площадь', max_length=255)
    phone = models.CharField(u'телефон', max_length=255)
    text = models.TextField(u'описание')
    franch_text = models.TextField(u'Текст на странице с франшизами', null=True, blank=True)
    latitude = models.CharField(u'широта', max_length=255)
    longitude = models.CharField(u'долгота', max_length=255)
    recipient_email = models.EmailField(u'email получателя', max_length=255)
    call_metrica_target = models.CharField(u'цель Я.Метрики для задать вопрос', max_length=255, null=True, blank=True)
    anchor = models.CharField(u'якорь', max_length=50, null=True, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'торговый центр Вологды'
        verbose_name_plural = u'торговые центры Вологды'
        ordering = ['weight', 'pk']


class VologdaMartImage(models.Model):

    mart = models.ForeignKey(VologdaMart, related_name='images')
    image = models.ImageField(u'изображение', upload_to='assets')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'Изображения'
        ordering = ['weight', 'pk']


class VologdaMartRecipientEmail(models.Model):

    city = models.ForeignKey(VologdaMart, related_name='recipients')
    email = models.EmailField(u'email', max_length=255)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'получатель'
        verbose_name_plural = u'получатели'


class VologdaBrend(models.Model):

    mart = models.ForeignKey(VologdaMart, related_name='brends')
    title = models.CharField(u'название', max_length=255, blank=True)
    image = models.ImageField(u'изображение', upload_to='assets')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'бренд'
        verbose_name_plural = u'бренды торгового центра'
        ordering = ['weight', 'pk']


class VologdaFeedback(models.Model):

    mart = models.ForeignKey(VologdaMart, verbose_name='ТЦ')
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


class PhotoReport(models.Model):

    city = models.ForeignKey(City, verbose_name=u'объект')
    title = models.CharField(u'название', max_length=255)
    image = models.ImageField(u'обложка', upload_to='assets_photos')
    publication_date = models.DateField(u'дата публикации')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('assets_photoreport_detail', args=[self.city.pk, self.pk])

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'фотоотчет'
        verbose_name_plural = u'фотоотчеты'
        ordering = ['-publication_date', '-created_at']


class Photo(models.Model):

    report = models.ForeignKey(PhotoReport, related_name='photos')
    image = models.ImageField(u'фотография', upload_to='assets_photos')

    class Meta:
        verbose_name = u'фотография'
        verbose_name_plural = u'фотографии'
        ordering = ['pk']


class FranchCity(models.Model):

    city = models.ForeignKey(City, verbose_name=u'ТЦ', related_name='franshes')
    name = models.CharField(u'название франшизы', max_length=255)
    partner = models.CharField(u'название партнера', max_length=255, blank=True, null=True)
    image = models.ImageField(u'изображение', upload_to='asserts')
    area = models.CharField(u'площадь', max_length=50, null=True)
    description = models.TextField(u'описание', null=True, blank=True)
    recipient_email = models.EmailField(u'контактный Email', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        reverse('assets_franch_list', args=[self.city.slug])

    class Meta:
        verbose_name = u'франшиза'
        verbose_name_plural = u'франшизы'
        ordering = ['weight', 'pk']


class FranchFeedback(models.Model):

    franch = models.ForeignKey(FranchCity, verbose_name='франшиза', null=True, blank=True)
    full_name = models.CharField(u'имя', max_length=255)
    phone = models.CharField(u'телефон', max_length=255, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'сообщение')
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'вопрос по франшизе'
        verbose_name_plural = u'вопросы по франшизе'
        ordering = ['-created_at']


class FranchVologda(models.Model):

    mart = models.ForeignKey(VologdaMart, verbose_name=u'ТЦ', related_name='franshes')
    name = models.CharField(u'название франшизы', max_length=255)
    partner = models.CharField(u'название партнера', max_length=255, blank=True, null=True)
    image = models.ImageField(u'изображение', upload_to='asserts')
    area = models.CharField(u'площадь', max_length=50, null=True)
    description = models.TextField(u'описание', null=True, blank=True)
    recipient_email = models.EmailField(u'контактный Email', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        reverse('assets_franchvologda_list', args=[self.mart.pk])

    class Meta:
        verbose_name = u'франшиза'
        verbose_name_plural = u'франшизы'
        ordering = ['weight', 'pk']


class FranchVologdaFeedback(models.Model):

    franch = models.ForeignKey(FranchVologda, verbose_name='франшиза', null=True, blank=True)
    full_name = models.CharField(u'имя', max_length=255)
    phone = models.CharField(u'телефон', max_length=255, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'сообщение')
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'вопрос по франшизе'
        verbose_name_plural = u'вопросы по франшизе'
        ordering = ['-created_at']

#=================
# ТЦ городов
class CityMart(models.Model):

    city = models.ForeignKey(City, related_name='marts')
    title = models.CharField(u'загололок', max_length=255)
    address = models.CharField(u'адрес', max_length=255, null=True)
    area = models.CharField(u'площадь', max_length=255, null=True)
    phone = models.CharField(u'телефон', max_length=255)
    text = models.TextField(u'описание')
    franch_text = models.TextField(u'Текст на странице с франшизами', null=True, blank=True)
    latitude = models.CharField(u'широта', max_length=255)
    longitude = models.CharField(u'долгота', max_length=255)
    recipient_email = models.EmailField(u'email получателя', max_length=255)
    call_metrica_target = models.CharField(u'цель Я.Метрики для задать вопрос', max_length=255, null=True, blank=True)
    anchor = models.CharField(u'якорь', max_length=50, null=True, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'торговый центр'
        verbose_name_plural = u'торговые центры'
        ordering = ['weight', 'pk']


class CityMartImage(models.Model):

    mart = models.ForeignKey(CityMart, related_name='images')
    image = models.ImageField(u'изображение', upload_to='assets')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'Изображения'
        ordering = ['weight', 'pk']


class CityMartRecipientEmail(models.Model):

    city = models.ForeignKey(CityMart, related_name='recipients')
    email = models.EmailField(u'email', max_length=255)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'получатель'
        verbose_name_plural = u'получатели'


class MartBrend(models.Model):

    mart = models.ForeignKey(CityMart, related_name='brends')
    title = models.CharField(u'название', max_length=255, blank=True)
    image = models.ImageField(u'изображение', upload_to='assets')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    class Meta:
        verbose_name = u'бренд ТЦ'
        verbose_name_plural = u'бренды торговых центров'
        ordering = ['weight', 'pk']


class MartFeedback(models.Model):

    mart = models.ForeignKey(CityMart, verbose_name='ТЦ')
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


class FranchMart(models.Model):

    mart = models.ForeignKey(CityMart, verbose_name=u'ТЦ', related_name='franshes')
    name = models.CharField(u'название франшизы', max_length=255)
    partner = models.CharField(u'название партнера', max_length=255, blank=True, null=True)
    image = models.ImageField(u'изображение', upload_to='asserts')
    area = models.CharField(u'площадь', max_length=50, null=True)
    description = models.TextField(u'описание', null=True, blank=True)
    recipient_email = models.EmailField(u'контактный Email', max_length=255)
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        reverse('assets_franchmart_list', args=[self.mart.pk])

    class Meta:
        verbose_name = u'франшиза'
        verbose_name_plural = u'франшизы'
        ordering = ['weight', 'pk']


class FranchMartFeedback(models.Model):

    franch = models.ForeignKey(FranchMart, verbose_name='франшиза', null=True, blank=True)
    full_name = models.CharField(u'имя', max_length=255)
    phone = models.CharField(u'телефон', max_length=255, blank=True)
    email = models.EmailField(u'email', max_length=255, blank=True)
    text = models.TextField(u'сообщение')
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = 'вопрос по франшизе'
        verbose_name_plural = u'вопросы по франшизе'
        ordering = ['-created_at']


@receiver(post_save, sender=CityMart)
def enable_has_marts(sender, instance, **kwargs):
    if kwargs.get('raw', False):
        return
    city = instance.city
    city.has_marts = True
    city.save()


@receiver(post_delete, sender=CityMart)
def unindex_vacancy(sender, instance, **kwargs):
    city = instance.city
    if not city.marts.exists():
        city.has_marts = False
        city.save()