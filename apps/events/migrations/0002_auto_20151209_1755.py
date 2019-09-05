# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorder',
            name='event',
            field=models.ForeignKey(related_name='orders', verbose_name='\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', to='events.Event'),
            preserve_default=True,
        ),
    ]
