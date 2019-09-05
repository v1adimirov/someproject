# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0039_city_city_recipient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='peview_2',
            field=models.TextField(null=True, verbose_name='\u0442\u0435\u0441\u0442 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435 \u0422\u0426 \u0438 \u0422\u0420\u0426', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='preview_image_2',
            field=models.ImageField(upload_to=b'assert', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043f\u0438\u0441\u043a\u0430 \u0422\u0426 \u0438 \u0422\u0420\u0426', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='title_2',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u0422\u0426 \u0438 \u0422\u0420\u0426', blank=True),
            preserve_default=True,
        ),
    ]
