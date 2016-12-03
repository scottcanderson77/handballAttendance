# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20161128_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='added_reports',
            field=models.ForeignKey(default=1, to='reports.report'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='title',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
