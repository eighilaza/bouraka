# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150930_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateTimeField(verbose_name='published on:', default=datetime.datetime.now),
        ),
    ]
