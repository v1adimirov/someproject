# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0044_city_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMartRecipientEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('city', models.ForeignKey(related_name='recipients', to='assets.CityMart')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CityRecipientEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('city', models.ForeignKey(related_name='recipients', to='assets.City')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VologdaMartRecipientEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('city', models.ForeignKey(related_name='recipients', to='assets.VologdaMart')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VologdaRecipientEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('city', models.ForeignKey(related_name='recipients', to='assets.VologdaCity')),
            ],
            options={
                'verbose_name': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
    ]
