# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0003_auto_20170815_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(upload_to=b'development', verbose_name='\u0438\u043a\u043e\u043d\u043a\u0430')),
                ('link', models.CharField(max_length=255, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('page', models.ForeignKey(related_name='variants', to='development.DevelpmentPage')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0432\u0430\u0440\u0438\u0430\u043d\u0442',
                'verbose_name_plural': '\u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='develpmentpage',
            name='text_var',
            field=models.TextField(default=b'', verbose_name='\u0422\u0435\u043a\u0441\u0442 "\u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430"', blank=True),
            preserve_default=True,
        ),
    ]
