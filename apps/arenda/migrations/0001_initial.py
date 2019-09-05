# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430')),
                ('is_new', models.BooleanField(default=False, verbose_name='\u0430\u0440\u0435\u043d\u0434\u0430 \u0432 \u0441\u0442\u0440\u043e\u044f\u0449\u0438\u0445\u0441\u044f')),
                ('is_old', models.BooleanField(default=False, verbose_name='\u0430\u0440\u0435\u043d\u0434\u0430 \u0432 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445')),
                ('position', models.CharField(max_length=255, verbose_name='\u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c')),
                ('phones', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b')),
                ('cities', models.CharField(max_length=255, verbose_name='\u0433\u043e\u0440\u043e\u0434\u0430')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442',
                'verbose_name_plural': '\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactsEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('contacts', models.ForeignKey(related_name='emails', to='arenda.Contacts')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'email',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0446\u0435\u043d\u0442\u0440',
                'verbose_name_plural': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c', blank=True)),
                ('products', models.CharField(max_length=255, verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u043e\u0432', blank=True)),
                ('comment', models.TextField(verbose_name='\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0440\u0430\u0438\u0439', blank=True)),
                ('full_name', models.TextField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('company', models.CharField(max_length=255, verbose_name='\u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044f', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('mart', models.ForeignKey(verbose_name='\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0446\u0435\u043d\u0442\u0440', blank=True, to='arenda.Mart', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
    ]
