# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20151031_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('city', models.ForeignKey(verbose_name=b'\xd0\xb3\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', to='assets.City', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0442\u043d\u043e\u0439 \u0441\u0432\u044f\u0437\u0438',
                'verbose_name_plural': '\u043e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u0432\u044f\u0437\u044c',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='city',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='ig_link',
            field=models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 Instagram', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='video_link',
            field=models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 YouTube', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='video_text',
            field=models.TextField(verbose_name='\u0442\u0435\u0441\u0442 \u043f\u043e\u0434 \u0432\u0438\u0434\u0435\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='city',
            name='video_title',
            field=models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u0438\u0434\u0435\u043e', blank=True),
            preserve_default=True,
        ),
    ]
