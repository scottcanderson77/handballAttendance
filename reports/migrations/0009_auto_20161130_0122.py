# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20161129_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='added_reports',
        ),
        migrations.AddField(
            model_name='folder',
            name='added_reports',
            field=models.ManyToManyField(to='reports.report'),
        ),
    ]
