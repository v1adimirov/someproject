# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_adv_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'vacancies', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('link', models.CharField(default=b'', max_length=500, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('title', models.CharField(default=b'', max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u044d\u043b\u0435\u043c\u0435\u043d\u0442 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
                'verbose_name_plural': '\u0441\u043b\u0430\u0439\u0434\u0435\u0440 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='adv',
            options={'ordering': ['weight'], 'verbose_name': '\u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432\u043e', 'verbose_name_plural': '\u043f\u0440\u0435\u0438\u043c\u0443\u0449\u0435\u0441\u0442\u0432\u0430'},
        ),
    ]
