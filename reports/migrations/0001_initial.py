# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=30)),
                ('detailed_description', models.CharField(max_length=200)),
                ('is_public', models.BooleanField(default=True)),
                ('is_private', models.BooleanField(default=False)),
            ],
        ),
    ]
