# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_auto_20161203_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='is_public',
        ),
    ]
