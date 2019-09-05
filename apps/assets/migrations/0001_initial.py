# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u0432\u043e\u043a')),
                ('city', models.CharField(max_length=255, verbose_name='\u0433\u043e\u0440\u043e\u0434')),
                ('slug', models.CharField(unique=True, max_length=255, verbose_name='slug')),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('area', models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('peview', models.TextField(verbose_name='\u0442\u0435\u0441\u0442 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('video_title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u0438\u0434\u0435\u043e')),
                ('video_link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 YouTube')),
                ('video_text', models.TextField(verbose_name='\u0442\u0435\u0441\u0442 \u043f\u043e\u0434 \u0432\u0438\u0434\u0435\u043e')),
                ('online_video', models.CharField(max_length=255, verbose_name='\u043e\u043d\u043b\u0430\u0439\u043d \u0442\u0440\u0430\u043d\u0441\u043b\u044f\u0446\u0438\u044f \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0430', blank=True)),
                ('presentation', models.FileField(upload_to=b'assets', null=True, verbose_name='\u043f\u0440\u0435\u0437\u0435\u043d\u0442\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0435\u043a\u0442\u0430', blank=True)),
                ('vk_link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u0412\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0435', blank=True)),
                ('yt_link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 YouTube', blank=True)),
                ('ig_link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 Instagram')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'city'],
                'verbose_name': '\u0433\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '\u0430\u043a\u0442\u0438\u0432\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0442\u0435\u0441\u0442')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='concepts', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f',
                'verbose_name_plural': '\u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0442\u0435\u0441\u0442')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='locations', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043b\u043e\u043a\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043b\u043e\u043a\u0430\u0446\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MapMarkCoords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('latitude', models.CharField(max_length=255, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430')),
                ('longitude', models.CharField(max_length=255, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430')),
                ('city', models.ForeignKey(related_name='marks', to='assets.City')),
            ],
            options={
                'verbose_name': '\u043c\u0435\u0442\u043a\u0430',
                'verbose_name_plural': '\u043c\u0435\u0442\u043a\u0438 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=255, verbose_name='\u0446\u0438\u0444\u0440\u0430')),
                ('note', models.CharField(max_length=255, verbose_name='\u043f\u043e\u0434\u043f\u0438\u0441\u044c')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='numbers', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0446\u0438\u0444\u0440\u0430',
                'verbose_name_plural': '\u0446\u0438\u0444\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(upload_to=b'mainpage', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='parthners', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043f\u0430\u0440\u0442\u043d\u0435\u0440',
                'verbose_name_plural': '\u043f\u0430\u0440\u0442\u043d\u0435\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043b\u0430\u043d\u0430')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='plans', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043f\u043b\u0430\u043d',
                'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u043b\u0430\u043d\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assetimage',
            name='city',
            field=models.ForeignKey(related_name='images', to='assets.City'),
            preserve_default=True,
        ),
    ]
