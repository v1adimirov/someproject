# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0037_auto_20160613_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='FranchMartFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='\u0438\u043c\u044f')),
                ('phone', models.CharField(max_length=255, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='email', blank=True)),
                ('text', models.TextField(verbose_name='\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438')),
                ('franch', models.ForeignKey(verbose_name=b'\xd1\x84\xd1\x80\xd0\xb0\xd0\xbd\xd1\x88\xd0\xb8\xd0\xb7\xd0\xb0', blank=True, to='assets.FranchMart', null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0432\u043e\u043f\u0440\u043e\u0441 \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
                'verbose_name_plural': '\u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043f\u043e \u0444\u0440\u0430\u043d\u0448\u0438\u0437\u0435',
            },
            bases=(models.Model,),
        ),
    ]
