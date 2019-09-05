# coding: utf-8
import lemon

from .models import Vacancy, City, ContactPerson, Adv, Resume, SliderItem, Question


class VacancyAdmin(lemon.ModelAdmin):

    list_display = ['position', 'city']
    list_filter = ['city']
    markup_fields = ['requirements', 'duties', 'conditions', 'contacts']


class ContactPersonAdmin(lemon.ModelAdmin):

    list_display = ['full_name', 'weight']
    list_editable = ['weight']


class SliderItemAdmin(lemon.ModelAdmin):

    list_display = ['id','title', 'link', 'is_active', 'weight']
    list_editable = ['weight']


class AdvAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight']
    list_editable = ['weight']

class ResumeAdmin(lemon.ModelAdmin):

    list_display = ['id', 'last_name', 'phone','email']



lemon.site.register(City)
lemon.site.register(SliderItem, SliderItemAdmin)
lemon.site.register(Adv, AdvAdmin)
lemon.site.register(Resume, ResumeAdmin)
lemon.site.register(Question)
lemon.site.register(Vacancy, VacancyAdmin)
lemon.site.register(ContactPerson, ContactPersonAdmin)
