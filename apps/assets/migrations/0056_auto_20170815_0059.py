# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0055_auto_20170815_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ImageField(upload_to=b'assert', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='contact_person2',
            field=models.CharField(max_length=255, null=True, verbose_name='\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='contact_photo2',
            field=models.ImageField(upload_to=b'assert', null=True, verbose_name='\u0444\u043e\u0442\u043e \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0433\u043e \u043b\u0438\u0446\u0430 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='email2',
            field=models.EmailField(max_length=255, null=True, verbose_name='email 2', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='phone2',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d 2', blank=True),
            preserve_default=True,
        ),
    ]
