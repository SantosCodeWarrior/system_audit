# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0006_auto_20230922_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_tracker',
            name='taxable',
            field=models.CharField(max_length=220, null=True),
        ),
    ]
