# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse


class City(models.Model):

    title = models.CharField(u'название', max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'город'
        verbose_name_plural = u'города'
        ordering = ['title']


class Adv(models.Model):

    title = models.CharField(u'заголовок', max_length=255)
    description = models.TextField(u'описание', blank=True, default="")
    image = models.ImageField(u'изображение', null=True, blank=True,
                              upload_to='vacancies')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'преимущество'
        verbose_name_plural = u'преимущества'
        ordering = ['weight',]


class SliderItem(models.Model):

    image = models.ImageField(u'изображение', upload_to='vacancies')
    link = models.CharField(u'ссылка', default="", max_length=500, blank=True)
    title = models.CharField(u'заголовок', default="",max_length=255, blank=True)
    date = models.CharField(u'дата', default="",max_length=255, blank=True)
    comment = models.CharField(u'подпись', default="",max_length=255, blank=True)
    weight = models.PositiveIntegerField(u'сортировка', default=100)
    is_active = models.BooleanField(u'активный', default=True)

    def __unicode__(self):
        return self.title or self.image.url

    class Meta:
        verbose_name = u'элемент слайдера'
        verbose_name_plural = u'слайдер'
        ordering = ['weight', 'pk']


class Vacancy(models.Model):

    city = models.ForeignKey(City, verbose_name=u'город')
    position = models.CharField(u'должность', max_length=255)
    requirements = models.TextField(u'требования')
    duties = models.TextField(u'обязанности')
    conditions = models.TextField(u'условия работы', blank=True)
    contacts = models.TextField(u'контакты')

    def get_absolute_url(self):
        return reverse('vacancies_vacancy_detail', args=[self.pk])

    def __unicode__(self):
        return self.position

    class Meta:
        verbose_name = u'вакансия'
        verbose_name_plural = u'вакансии'
        ordering = ['city', 'pk']


class Resume(models.Model):

    first_name = models.CharField(u'Имя', default="", blank=True, max_length=255)
    last_name = models.CharField(u'Фамилия', default="", blank=True, max_length=255)
    phone = models.CharField(u'Телефон', default="", blank=True, max_length=255)
    email = models.EmailField(u'Email', default="", blank=True, max_length=255)
    experience = models.TextField(verbose_name=u'Кратко о Вашем опыте', default="", blank=True)
    file = models.FileField(u'Прикрепленный файл', blank=True,upload_to='vacancies', null=True)
    # created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = u'резюме'
        verbose_name_plural = u'резюме'
        ordering = ['-id']

class Question(models.Model):

    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    phone = models.CharField(u'Телефон', max_length=255)
    email = models.EmailField(u'Email', max_length=255)
    question = models.TextField(verbose_name=u'Ваш вопрос')
    created_at = models.DateTimeField(u'дата отправки', auto_now_add=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'
        ordering = ['-created_at']


class ContactPerson(models.Model):

    full_name = models.CharField(u'ФИО', max_length=255)
    position = models.CharField(u'должность', max_length=255)
    phones = models.CharField(u'телефоны', max_length=255,
                              help_text="Номера телефонов разделяются запятой")
    email = models.EmailField(u'email', max_length=255, null=True, blank=True)
    image = models.ImageField(u'изображение',null=True, blank=True, upload_to='vacancies/persons')
    weight = models.PositiveIntegerField(u'сортировка', default=100)

    def __unicode__(self):
        return self.full_name

    def get_phones(self):
        return self.phones.split(",")

    class Meta:
        verbose_name = u'контактное лицо'
        verbose_name_plural = u'контакты'
        ordering = ['weight', 'pk']
