# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_adv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='image',
            field=models.ImageField(upload_to=b'vacancies', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
