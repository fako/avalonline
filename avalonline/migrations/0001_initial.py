# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('qr_code', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('black', 'black'), ('white', 'white')], max_length=50)),
                ('game', models.ForeignKey(to='avalonline.Game', related_name='players')),
            ],
        ),
    ]
