# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043e\u0442 \u043a\u043e\u0433\u043e')),
                ('image', models.ImageField(upload_to=b'reviews', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u043e\u0442\u0437\u044b\u0432\u0430')),
                ('on_main', models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439')),
                ('on_act', models.BooleanField(default=False, verbose_name='\u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0433\u043e \u0446\u0435\u043d\u0442\u0440\u0430')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u043e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('video_link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e')),
                ('image', models.ImageField(upload_to=b'reviews', verbose_name='\u043e\u0431\u043b\u043e\u0436\u043a\u0430 \u0432\u0438\u0434\u0435\u043e')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0432\u0438\u0434\u0435\u043e \u043e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u0432\u0438\u0434\u0435\u043e \u043e\u0442\u0437\u044b\u0432\u044b',
            },
            bases=(models.Model,),
        ),
    ]
