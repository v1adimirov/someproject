# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=255, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('experience', models.TextField(verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e \u043e \u0412\u0430\u0448\u0435\u043c \u043e\u043f\u044b\u0442\u0435')),
                ('file', models.FileField(upload_to=b'vacancies', verbose_name='\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0440\u0435\u0437\u044e\u043c\u0435',
                'verbose_name_plural': '\u0440\u0435\u0437\u044e\u043c\u0435',
            },
            bases=(models.Model,),
        ),
    ]
