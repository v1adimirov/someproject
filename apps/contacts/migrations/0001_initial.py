# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=255, verbose_name='\u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('phones', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b')),
                ('email', models.CharField(max_length=255, verbose_name='email')),
                ('email2', models.CharField(max_length=255, verbose_name='email 2', blank=True)),
                ('email3', models.CharField(max_length=255, verbose_name='email 3', blank=True)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('is_active', models.BooleanField(max_length=255, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('category', models.ForeignKey(verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='contacts.Category')),
            ],
            options={
                'ordering': ['category', 'subcategory', 'weight', 'pk'],
                'verbose_name': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e',
                'verbose_name_plural': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432',
                'verbose_name_plural': '\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='subcategory',
            field=models.ForeignKey(verbose_name='\u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', blank=True, to='contacts.SubCategory', null=True),
            preserve_default=True,
        ),
    ]
