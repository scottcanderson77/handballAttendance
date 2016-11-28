# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_report_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='uploaded_at',
            field=models.DateTimeField(default='9999-01-01'),
        ),
    ]
