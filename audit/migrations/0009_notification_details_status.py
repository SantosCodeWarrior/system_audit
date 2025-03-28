# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0008_auto_20230925_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_details',
            name='status',
            field=models.CharField(max_length=520, null=True),
        ),
    ]
