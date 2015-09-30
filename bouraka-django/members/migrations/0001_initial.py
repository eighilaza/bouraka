# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150, blank=True)),
                ('title', models.CharField(max_length=150, blank=True)),
                ('team', models.CharField(max_length=150, blank=True)),
                ('departement', models.CharField(max_length=150, blank=True)),
                ('year', models.IntegerField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='members')),
                ('order', models.IntegerField()),
            ],
        ),
    ]
