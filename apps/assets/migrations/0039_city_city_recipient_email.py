# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0038_franchmartfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_recipient_email',
            field=models.EmailField(max_length=255, verbose_name='email \u0434\u043b\u044f \u0432\u043e\u043f\u0440\u043e\u0441\u043e\u0432 \u043e\u0431\u0449\u0438\u0439 \u0434\u043b\u044f \u0433\u043e\u0440\u043e\u0434\u0430 (\u0432 \u0441\u043b\u0443\u0447\u0430\u0435 \u043d\u0435\u0441\u043a\u043b\u044c\u043a\u0438\u0445 \u0422\u0426)', blank=True),
            preserve_default=True,
        ),
    ]
