# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150, blank=True)),
                ('group', models.CharField(max_length=150, blank=True)),
                ('website', models.CharField(max_length=150, blank=True)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='sponsors')),
                ('order', models.IntegerField()),
            ],
        ),
    ]
