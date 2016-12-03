# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0014_remove_report_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='is_encrypted',
            field=models.BooleanField(),
        ),
    ]
