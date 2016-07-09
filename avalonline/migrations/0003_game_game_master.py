# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avalonline', '0002_auto_20160709_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_master',
            field=models.ForeignKey(null=True, related_name='+', blank=True, to='avalonline.Player'),
        ),
    ]
