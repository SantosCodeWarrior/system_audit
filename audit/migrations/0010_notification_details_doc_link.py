# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0009_notification_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_details',
            name='doc_link',
            field=models.CharField(max_length=520, null=True),
        ),
    ]
