# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_monthly_tracker_taxable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_tracker',
            name='taxable',
            field=models.FloatField(null=True),
        ),
    ]
