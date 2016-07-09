# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalonline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='role',
            field=models.CharField(null=True, max_length=50, blank=True, choices=[('black', 'black'), ('white', 'white')]),
        ),
    ]
