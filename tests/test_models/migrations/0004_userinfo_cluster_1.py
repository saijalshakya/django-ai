# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_models', '0003_add_avg_times_clusters'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='cluster_1',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Cluster 1'),
        ),
    ]
