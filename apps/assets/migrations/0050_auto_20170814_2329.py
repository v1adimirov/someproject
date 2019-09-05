# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_images(apps, schema_editor):
    VologdaMart = apps.get_model('assets', 'VologdaMart')
    VologdaMartImage = apps.get_model('assets', 'VologdaMartImage')
    for obj in VologdaMart.objects.all():
        VologdaMartImage.objects.create(
            image=obj.image,
            mart=obj
        )


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0049_vologdamartimage'),
    ]

    operations = [
        migrations.RunPython(move_images),
    ]
