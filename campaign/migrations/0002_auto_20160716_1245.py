# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 12:45
from __future__ import unicode_literals

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='charity',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='campaign.Charity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='campaign',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='campaign.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='created',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='raised',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='description',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='charity',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=b'name'),
        ),
    ]
