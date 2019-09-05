# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0047_mapmarkcoords_mark_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityReward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('text', models.TextField(verbose_name='\u043f\u043e\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430\u0433\u0440\u0430\u0434\u044b')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='rewards', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043d\u0430\u0433\u0440\u0430\u0434\u0430',
                'verbose_name_plural': '\u0434\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
