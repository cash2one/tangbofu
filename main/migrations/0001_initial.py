# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=255)),
                ('desc', models.TextField(default=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
            ],
        ),
    ]
