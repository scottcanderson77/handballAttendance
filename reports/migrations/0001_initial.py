# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(default='title', max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('short_description', models.CharField(max_length=30)),
                ('detailed_description', models.CharField(max_length=200)),
                ('is_private', models.BooleanField(default='False')),
                ('location', models.CharField(default='Virginia', max_length=100)),
                ('is_encrypted', models.BooleanField(default='False')),
                ('document', models.FileField(default='document', upload_to='documents/')),
                ('username_id', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='added_reports',
            field=models.ManyToManyField(to='reports.report'),
        ),
        migrations.AddField(
            model_name='folder',
            name='username_id',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
