# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_vologdamart_recipient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='preview_image',
            field=models.ImageField(upload_to=b'assert', null=True, verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043f\u0438\u0441\u043a\u0430'),
            preserve_default=True,
        ),
    ]
