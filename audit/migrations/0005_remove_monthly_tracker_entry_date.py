# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0004_monthly_tracker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthly_tracker',
            name='entry_date',
        ),
    ]
