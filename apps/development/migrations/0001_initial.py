# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'development', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f')),
                ('year', models.CharField(max_length=10, verbose_name='\u0433\u043e\u0434')),
                ('addr', models.TextField(verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('props', models.TextField(verbose_name='\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0438\u043a\u043e\u043d\u043a\u0430',
                'verbose_name_plural': '\u0438\u043a\u043e\u043d\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DevelpmentPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('about_title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a "\u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438"')),
                ('about_text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
                ('text2', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 2')),
                ('contacts', models.TextField(verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd1\x8b')),
                ('recepient', models.EmailField(max_length=255, verbose_name='\u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c \u043f\u0438\u0441\u0435\u043c \u0438\u0437 \u0444\u043e\u0440\u043c\u044b')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0420\u0430\u0437\u0432\u0438\u0442\u0438\u0435',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u0420\u0430\u0437\u0432\u0438\u0442\u0438\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(max_length=50, verbose_name='\u0438\u043a\u043e\u043d\u043a\u0430', choices=[(b'_development', '\u0434\u0435\u0432\u0435\u043b\u043e\u043f\u043c\u0435\u043d\u0442 \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438'), (b'_retail', '\u0440\u0438\u0442\u0435\u0439\u043b'), (b'_distribution', '\u0434\u0438\u0441\u0442\u0440\u0438\u0431\u044c\u044e\u0446\u0438\u044f')])),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('page', models.ForeignKey(related_name='directions', to='development.DevelpmentPage')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.CharField(max_length=50, verbose_name='\u0438\u043a\u043e\u043d\u043a\u0430', choices=[(b'_1', '\u0441\u0442\u0440\u043e\u0438\u043c'), (b'_2', '\u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0440\u0443\u0435\u043c'), (b'_3', '\u0443\u043f\u0440\u0430\u0432\u043b\u044f\u0435\u043c')])),
                ('title', models.CharField(max_length=500, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('page', models.ForeignKey(related_name='icons', to='development.DevelpmentPage')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0438\u043a\u043e\u043d\u043a\u0430',
                'verbose_name_plural': '\u0438\u043a\u043e\u043d\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('page', models.ForeignKey(related_name='links', to='development.DevelpmentPage')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('text', models.TextField(null=True, verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438',
                'verbose_name_plural': '\u043e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('weight', models.PositiveIntegerField(default=100)),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0433\u043e\u0440\u043e\u0434 \u0432 \u0437\u0430\u044f\u0432\u043a\u0435',
                'verbose_name_plural': '\u0433\u043e\u0440\u043e\u0434\u0430 \u0432 \u0437\u0430\u044f\u0432\u043a\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('weight', models.PositiveIntegerField(default=100)),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043e\u0431\u044a\u0435\u043a\u0442 \u0432 \u0437\u0430\u044f\u0432\u043a\u0435',
                'verbose_name_plural': '\u043e\u0431\u044a\u0435\u043a\u0442\u044b \u0432 \u0437\u0430\u044f\u0432\u043a\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.ForeignKey(verbose_name=b'\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True, to='development.OrderCity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='obj',
            field=models.ForeignKey(verbose_name=b'\xd0\xbe\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xba\xd1\x82', blank=True, to='development.OrderObject', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='page',
            field=models.ForeignKey(related_name='assets', to='development.DevelpmentPage'),
            preserve_default=True,
        ),
    ]
