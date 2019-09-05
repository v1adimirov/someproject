# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_vologdamart_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='VologdaCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'assets', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('preview', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435')),
                ('text', models.TextField(verbose_name='\u0442\u0435\u043a\u0441\u0442')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043b\u043e\u0433\u0434\u0430',
                'verbose_name_plural': '\u0412\u043e\u043b\u043e\u0433\u0434\u0430',
            },
            bases=(models.Model,),
        ),
    ]
