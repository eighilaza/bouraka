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
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(blank=True, max_length=4, choices=[(b'BIM', b'BIM'), (b'BS', b'BS'), (b'GCU', b'GCU'), (b'GE', b'GE'), (b'GEN', b'GEN'), (b'GI', b'GI'), (b'GMC', b'GMC'), (b'GMD', b'GMD'), (b'GMPP', b'GMPP'), (b'IF', b'IF'), (b'PC', b'PC'), (b'SGM', b'SGM'), (b'TC', b'TC')])),
                ('school_year', models.CharField(blank=True, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')])),
                ('phone_number', models.CharField(max_length=13, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(unique=True, max_length=200)),
                ('team_manager', models.ForeignKey(related_name='+', blank=True, to='members.Member', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='teams',
            field=models.ManyToManyField(to='members.Team', blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
