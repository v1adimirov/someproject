# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0036_city_list_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='franchmartfeedback',
            name='franch',
        ),
        migrations.DeleteModel(
            name='FranchMartFeedback',
        ),
    ]
