# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0022_auto_20160507_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='vologdacity',
            name='recipient_email',
            field=models.EmailField(default=b'kits@maxi-net.ru', max_length=255, verbose_name='Email \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f'),
            preserve_default=True,
        ),
    ]
