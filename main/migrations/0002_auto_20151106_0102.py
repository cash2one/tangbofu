# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=models.CharField(default=b'\xe6\x8f\x8f\xe8\xbf\xb0', max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=50),
        ),
    ]
