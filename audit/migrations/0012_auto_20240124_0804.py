# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0011_weekly_entry_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weekly_entry',
            old_name='remark',
            new_name='office365',
        ),
    ]
