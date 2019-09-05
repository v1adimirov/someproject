# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_auto_20151224_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.TextField(verbose_name='\u043a\u043e\u0434 \u043a\u0430\u043c\u0435\u0440\u044b')),
                ('city', models.ForeignKey(related_name='cameras', to='assets.City')),
            ],
            options={
                'verbose_name': '\u043a\u0430\u043c\u0435\u0440\u0430 \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u043c\u0435\u0440\u044b \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
    ]
