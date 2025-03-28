# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0010_notification_details_doc_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekly_entry',
            name='remark',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
