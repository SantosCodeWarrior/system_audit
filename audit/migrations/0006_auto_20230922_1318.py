# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0005_remove_monthly_tracker_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_tracker',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='monthly_tracker',
            name='nature_expense',
            field=models.CharField(max_length=220, null=True),
        ),
    ]
