# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0015_auto_20151219_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'assets_photos', verbose_name='\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f',
                'verbose_name_plural': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to=b'assets_photos', verbose_name='\u043e\u0431\u043b\u043e\u0436\u043a\u0430')),
                ('publication_date', models.DateField(verbose_name='\u0434\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(verbose_name='\u043e\u0431\u044a\u0435\u043a\u0442', to='assets.City')),
            ],
            options={
                'ordering': ['-publication_date', '-created_at'],
                'verbose_name': '\u0444\u043e\u0442\u043e\u043e\u0442\u0447\u0435\u0442',
                'verbose_name_plural': '\u0444\u043e\u0442\u043e\u043e\u0442\u0447\u0435\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='report',
            field=models.ForeignKey(related_name='photos', to='assets.PhotoReport'),
            preserve_default=True,
        ),
    ]
