# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('publication_date', models.DateTimeField(verbose_name='published on:', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('news', models.ForeignKey(to='news.News')),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='new',
        ),
        migrations.RemoveField(
            model_name='video',
            name='new',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='New',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
