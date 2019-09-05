# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0026_auto_20160510_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='FranchCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b')),
                ('partner', models.CharField(max_length=255, null=True, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430', blank=True)),
                ('image', models.ImageField(upload_to=b'asserts', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('description', models.TextField(null=True, verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
                ('recipient_email', models.EmailField(max_length=255, verbose_name='\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 Email')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('city', models.ForeignKey(related_name='franshes', verbose_name='\u0422\u0426', to='assets.City')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0430',
                'verbose_name_plural': '\u0444\u0440\u0430\u043d\u0448\u0438\u0437\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FranchFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('franch', models.ForeignKey(verbose_name=b'\xd1\x84\xd1\x80\xd0\xb0\xd0\xbd\xd1\x88\xd0\xb8\xd0\xb7\xd0\xb0', blank=True, to='assets.FranchCity', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
                'verbose_name_plural': '\u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='franch_text',
            field=models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0441 \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0430\u043c\u0438', blank=True),
            preserve_default=True,
        ),
    ]
