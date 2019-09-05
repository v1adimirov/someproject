# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_remove_videoreview_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoreview',
            name='video_image',
            field=models.ImageField(upload_to=b'reviews', null=True, verbose_name='\u043f\u0440\u0435\u0432\u044c\u044e \u0432\u0438\u0434\u0435\u043e\u0440\u043e\u043b\u0438\u043a\u0430', blank=True),
            preserve_default=True,
        ),
    ]
