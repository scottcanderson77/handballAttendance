# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_folder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='name',
            new_name='title',
        ),
    ]
