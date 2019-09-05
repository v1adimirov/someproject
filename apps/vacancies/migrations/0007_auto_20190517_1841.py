# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_auto_20190517_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideritem',
            options={'ordering': ['weight', 'pk'], 'verbose_name': '\u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430', 'verbose_name_plural': '\u0441\u043b\u0430\u0439\u0434\u0435\u0440'},
        ),
        migrations.AddField(
            model_name='contactperson',
            name='image',
            field=models.ImageField(upload_to=b'vacancies/persons', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
