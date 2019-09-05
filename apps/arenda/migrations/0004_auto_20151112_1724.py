# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arenda', '0003_auto_20151103_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='trademark',
            field=models.CharField(max_length=255, verbose_name='\u0442\u043e\u0440\u0433\u043e\u0432\u0430\u044f \u043c\u0430\u0440\u043a\u0430', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='whence',
            field=models.CharField(max_length=255, verbose_name='\u043e\u0442\u043a\u0443\u0434\u0430 \u0432\u044b \u0443\u0437\u043d\u0430\u043b\u0438 \u043e \u0422\u0420\u0426', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='area',
            field=models.CharField(max_length=255, verbose_name='\u043f\u043b\u043e\u0449\u0430\u0434\u044c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='mart',
            field=models.ForeignKey(verbose_name='\u0442\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0446\u0435\u043d\u0442\u0440', to='arenda.Mart', null=True),
            preserve_default=True,
        ),
    ]
