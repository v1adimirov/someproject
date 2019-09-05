# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_city_recipient_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='VologdaBrend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': '\u0431\u0440\u0435\u043d\u0434',
                'verbose_name_plural': '\u0431\u0440\u0435\u043d\u0434\u044b \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0433\u043e \u0446\u0435\u043d\u0442\u0440\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VologdaFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('latitude', models.CharField(max_length=255, verbose_name='\u0448\u0438\u0440\u043e\u0442\u0430')),
                ('longitude', models.CharField(max_length=255, verbose_name='\u0434\u043e\u043b\u0433\u043e\u0442\u0430')),
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
            name='VologdaMart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u043b\u043e\u043a')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('area', models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('text', models.TextField(verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0446\u0435\u043d\u0442\u0440 \u0412\u043e\u043b\u043e\u0433\u0434\u044b',
                'verbose_name_plural': '\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b \u0412\u043e\u043b\u043e\u0433\u0434\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='vologdafeedback',
            name='mart',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xa6', to='assets.VologdaMart'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vologdabrend',
            name='mart',
            field=models.ForeignKey(related_name='brends', to='assets.VologdaMart'),
            preserve_default=True,
        ),
    ]
