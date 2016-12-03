# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0012_auto_20161203_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
