# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_body',
            field=models.CharField(max_length=1000000),
        ),
    ]
