# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0003_user_entry_date_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='monthly_tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billing_date', models.DateField(null=True)),
                ('service_provider', models.CharField(max_length=220, null=True)),
                ('staff_member', models.CharField(max_length=220, null=True)),
                ('bill_no', models.CharField(max_length=220, null=True)),
                ('nature_expense', models.DateField(null=True)),
                ('amount_usd', models.FloatField(null=True)),
                ('amount_sgd', models.FloatField(null=True)),
                ('amount_euro', models.FloatField(null=True)),
                ('amount_inr', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('remarks', models.CharField(max_length=220, null=True)),
                ('entry_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
    ]
