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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, default='title')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=30)),
                ('detailed_description', models.CharField(max_length=200)),
                ('is_public', models.BooleanField(default=True)),
                ('is_private', models.BooleanField(default=False)),
                ('status_state', models.CharField(max_length=100, default='public')),
                ('location', models.CharField(max_length=100, default='Virginia')),
                ('is_encrypted', models.BooleanField(default=False)),
                ('document', models.FileField(upload_to='documents/', default='document')),
                ('uploaded_at', models.DateTimeField(default='time')),
            ],
        ),
    ]
