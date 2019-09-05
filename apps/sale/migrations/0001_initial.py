# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'sale', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('address', models.CharField(max_length=255, verbose_name='\u0430\u0434\u0440\u0435\u0441')),
                ('image', models.ImageField(upload_to=b'sale', verbose_name='\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('preview', models.TextField(verbose_name='\u043a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('content', models.TextField(verbose_name='\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('type', models.CharField(max_length=255, verbose_name='\u0442\u0438\u043f')),
                ('area', models.CharField(max_length=50, verbose_name='\u0437\u0435\u043c\u0435\u043b\u044c\u043d\u044b\u0439 \u0443\u0447\u0430\u0441\u0442\u043e\u043a, \u043a\u0432.\u043c.')),
                ('gba', models.CharField(max_length=50, verbose_name='GBA \u043a\u0432.\u043c.')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u043e\u0431\u044a\u0435\u043a\u0442 \u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0443',
                'verbose_name_plural': '\u043e\u0431\u044a\u0435\u043a\u0442\u044b \u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0443',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SaleProperty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('value', models.CharField(max_length=255, verbose_name='\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430')),
                ('sale', models.ForeignKey(related_name='properties', to='sale.SaleObject')),
            ],
            options={
                'ordering': ['weight', 'pk'],
                'verbose_name': '\u0441\u0432\u043e\u0439\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u043f\u0440\u043e\u0447\u0438\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saleimage',
            name='sale',
            field=models.ForeignKey(related_name='images', to='sale.SaleObject'),
            preserve_default=True,
        ),
    ]
