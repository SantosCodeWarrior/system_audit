# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0014_gst_bills_tracker_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gst_bills_tracker',
            name='warranty_time',
            field=models.FloatField(null=True),
        ),
    ]
