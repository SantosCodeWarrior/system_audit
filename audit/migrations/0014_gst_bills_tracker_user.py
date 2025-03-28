# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0013_gst_bills_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='gst_bills_tracker',
            name='user',
            field=models.ForeignKey(to='audit.User_entry', null=True),
        ),
    ]
