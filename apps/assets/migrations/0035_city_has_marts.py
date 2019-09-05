# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0034_citymart_franchmart_franchmartfeedback_martbrend_martfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='has_marts',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
