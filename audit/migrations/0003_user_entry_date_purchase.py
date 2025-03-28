# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0002_notification_details_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_entry',
            name='date_purchase',
            field=models.DateField(null=True),
        ),
    ]
