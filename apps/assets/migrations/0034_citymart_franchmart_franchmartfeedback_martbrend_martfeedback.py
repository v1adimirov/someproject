# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0033_city_quetion_metrica_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u043b\u043e\u043a')),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('area', models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('text', models.TextField(verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('franch_text', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0441 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0430\u043c\u0438', blank=True)),
                ('latitude', models.CharField(max_length=255, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430')),
                ('longitude', models.CharField(max_length=255, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430')),
                ('recipient_email', models.EmailField(max_length=255, verbose_name='email \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f')),
                ('call_metrica_target', models.CharField(max_length=255, null=True, verbose_name='\u0446\u0435\u043b\u044c \u042f.\u041c\u0435\u0442\u0440\u0438\u043a\u0438 \u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441', blank=True)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='marts', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0446\u0435\u043d\u0442\u0440',
                'verbose_name_plural': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FranchMart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b')),
                ('partner', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430', blank=True)),
                ('image', models.ImageField(upload_to=b'asserts', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('area', models.CharField(max_length=50, null=True, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('description', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('recipient_email', models.EmailField(max_length=255, verbose_name='\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 Email')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('mart', models.ForeignKey(related_name='franshes', verbose_name='\u0422\u0426', to='assets.CityMart')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0430',
                'verbose_name_plural': '\u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FranchMartFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('franch', models.ForeignKey(verbose_name=b'\xd1\x84\xd1\x80\xd0\xb0\xd0\xbd\xd1\x88\xd0\xb8\xd0\xb7\xd0\xb0', blank=True, to='assets.FranchVologda', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
                'verbose_name_plural': '\u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MartBrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('mart', models.ForeignKey(related_name='brends', to='assets.CityMart')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0431\u0440\u0435\u043d\u0434 \u0422\u0426',
                'verbose_name_plural': '\u0431\u0440\u0435\u043d\u0434\u044b \u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0445 \u0446\u0435\u043d\u0442\u0440\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MartFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('mart', models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xa6', to='assets.CityMart')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438',
                'verbose_name_plural': '\u043e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c',
            },
            bases=(models.Model,),
        ),
    ]
