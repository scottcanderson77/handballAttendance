# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_folder_username_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='status_state',
        ),
        migrations.AlterField(
            model_name='report',
            name='is_private',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='is_public',
            field=models.BooleanField(),
        ),
    ]
