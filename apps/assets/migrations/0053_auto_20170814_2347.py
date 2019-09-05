# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_images(apps, schema_editor):
    CityMart = apps.get_model('assets', 'CityMart')
    CityMartImage = apps.get_model('assets', 'CityMartImage')
    for obj in CityMart.objects.all():
        CityMartImage.objects.create(
            image=obj.image,
            mart=obj
        )


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0052_citymartimage'),
    ]

    operations = [
        migrations.RunPython(move_images),
    ]
