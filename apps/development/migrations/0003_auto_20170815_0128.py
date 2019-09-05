# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('development', '0002_remove_develpmentpage_recepient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['weight', 'pk'], 'verbose_name': '\u043e\u0431\u044a\u0435\u043a\u0442\u044b', 'verbose_name_plural': '\u043e\u0431\u044a\u0435\u043a\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['weight', 'pk'], 'verbose_name': '\u0441\u0441\u043b\u044b\u043a\u0430', 'verbose_name_plural': '\u0441\u0441\u044b\u043b\u043a\u0438'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430 \u0432 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0438', 'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438 \u0432 \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='asset',
            name='link',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430'),
            preserve_default=True,
        ),
    ]
