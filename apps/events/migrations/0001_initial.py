# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('event_date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('description', models.TextField(verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('date_start', models.DateTimeField(verbose_name='\u0434\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 \u0437\u0430\u044f\u0432\u043e\u043a')),
                ('date_stop', models.DateTimeField(verbose_name='\u0434\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043f\u0440\u0438\u0435\u043c\u0430 \u0437\u0430\u044f\u0432\u043e\u043a')),
                ('program', models.FileField(upload_to=b'events', null=True, verbose_name='\u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f', blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435')),
            ],
            options={
                'ordering': ['-date_start', '-date_stop'],
                'verbose_name': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('company', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
                ('city', models.CharField(max_length=255, verbose_name='\u0433\u043e\u0440\u043e\u0434')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('message', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('event', models.ForeignKey(verbose_name='\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', to='events.Event')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430 \u043d\u0430 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438 \u043d\u0430 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('event', models.ForeignKey(related_name='transfers', verbose_name='\u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435', to='events.Event')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043f\u0440\u043e\u0435\u0437\u0434\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='eventorder',
            name='transfer',
            field=models.ForeignKey(verbose_name='\u0441\u043f\u043e\u0441\u043e\u0431 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438', blank=True, to='events.Transfer', null=True),
            preserve_default=True,
        ),
    ]
