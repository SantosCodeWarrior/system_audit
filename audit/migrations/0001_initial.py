# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import audit.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='asset_registers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateField(null=True)),
                ('asset_name', models.CharField(max_length=220, null=True)),
                ('asset_type', models.CharField(max_length=220, null=True)),
                ('state', models.CharField(max_length=220, null=True)),
                ('date_purchase', models.CharField(max_length=220, null=True)),
                ('expiry_date', models.CharField(max_length=220, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('remark', models.CharField(max_length=220, null=True)),
                ('assigned_to', models.CharField(max_length=200, null=True)),
                ('count', models.CharField(max_length=200, null=True)),
                ('serial_no', models.CharField(max_length=220, null=True)),
                ('particular', models.CharField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='email_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_user_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='emergency_contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=220, null=True)),
                ('contact_mobile', models.CharField(max_length=220, null=True)),
                ('contact_landline', models.CharField(max_length=220, null=True)),
                ('address', models.CharField(max_length=220, null=True)),
                ('remarks', models.CharField(max_length=220, null=True)),
                ('department', models.CharField(max_length=220, null=True)),
                ('entry_date', models.CharField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='equipment_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('label', models.CharField(max_length=100, null=True)),
                ('active', models.IntegerField(null=True)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('purchase_date', models.DateField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('issue_any', models.CharField(max_length=220, null=True)),
                ('party_name', models.CharField(max_length=100, null=True)),
                ('party_contact', models.CharField(max_length=100, null=True)),
                ('repaired_date', models.DateField(null=True)),
                ('mechanic_name', models.CharField(max_length=200, null=True)),
                ('mechanic_contact', models.CharField(max_length=100, null=True)),
                ('remarks', models.CharField(max_length=220, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('issue_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='inventory_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('particulars', models.CharField(max_length=220, null=True)),
                ('department', models.CharField(max_length=220, null=True)),
                ('repaired_date', models.DateField(null=True)),
                ('purchase_date', models.DateField(null=True)),
                ('assigned_date', models.DateField(null=True)),
                ('assigned_to', models.CharField(max_length=220, null=True)),
                ('status', models.CharField(max_length=220, null=True)),
                ('warranty', models.CharField(max_length=220, null=True)),
                ('brand_name', models.CharField(max_length=220, null=True)),
                ('location', models.CharField(max_length=220, null=True)),
                ('remarks', models.CharField(max_length=220, null=True)),
                ('entry_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='network_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_date', models.DateField(null=True)),
                ('break_down', models.DateTimeField(null=True)),
                ('name_mc', models.CharField(max_length=120, null=True)),
                ('reported_name', models.CharField(max_length=120, null=True)),
                ('network_operator', models.CharField(max_length=120, null=True)),
                ('problem_reported', models.CharField(max_length=120, null=True)),
                ('action_taken', models.CharField(max_length=120, null=True)),
                ('time_status', models.DateTimeField(null=True)),
                ('total_time_break_down', models.CharField(max_length=120, null=True)),
                ('internet_speed', models.CharField(max_length=120, null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='notification_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_date', models.DateField(null=True)),
                ('email_name', models.CharField(max_length=220, null=True)),
                ('sent_date', models.DateField(null=True)),
                ('amount', models.CharField(max_length=220, null=True)),
                ('payment_status', models.CharField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='plan_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_type', models.CharField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='register_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('register_date', models.DateField(null=True)),
                ('it_non', models.CharField(max_length=20, null=True)),
                ('fitting', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=20, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('user_allotted', models.CharField(max_length=20, null=True)),
                ('security_level', models.CharField(max_length=20, null=True)),
                ('maintenance', models.CharField(max_length=20, null=True)),
                ('record_date', models.DateField(null=True)),
                ('remarks', models.CharField(max_length=20, null=True)),
                ('audit_key', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='remainder_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('remainder_date', models.DateField(null=True)),
                ('office_period_date', models.CharField(max_length=20, null=True)),
                ('email_move_date', models.CharField(max_length=20, null=True)),
                ('remarks', models.CharField(max_length=20, null=True)),
                ('user_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='system_problem_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('called_date', models.DateField(null=True)),
                ('party_name', models.CharField(max_length=220, null=True)),
                ('party_contact', models.CharField(max_length=220, null=True)),
                ('mechanic_name', models.CharField(max_length=220, null=True)),
                ('mechanic_number', models.CharField(max_length=220, null=True)),
                ('problems', models.CharField(max_length=220, null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='system_wfh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('remarks', models.CharField(max_length=220, null=True)),
                ('issue_date', models.DateField(null=True)),
                ('receive_date', models.DateField(null=True)),
                ('user_name', models.CharField(max_length=220, null=True)),
                ('cpu', models.CharField(max_length=220, null=True)),
                ('keyboard', models.CharField(max_length=220, null=True)),
                ('ups', models.CharField(max_length=220, null=True)),
                ('monitor', models.CharField(max_length=220, null=True)),
                ('headphone', models.CharField(max_length=220, null=True)),
                ('mouse', models.CharField(max_length=220, null=True)),
                ('department', models.CharField(max_length=220, null=True)),
                ('hdmi_cable', models.CharField(max_length=220, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('processor', models.CharField(max_length=200, null=True)),
                ('ram', models.CharField(max_length=200, null=True)),
                ('hdd', models.CharField(max_length=200, null=True)),
                ('keyboard', models.CharField(max_length=200, null=True)),
                ('mouse', models.CharField(max_length=200, null=True)),
                ('smps', models.CharField(max_length=200, null=True)),
                ('monitor', models.CharField(max_length=200, null=True)),
                ('operating_sys', models.CharField(max_length=200, null=True)),
                ('remark', models.CharField(max_length=200, null=True)),
                ('current_date', models.DateField(null=True)),
                ('items', models.FileField(null=True, upload_to=audit.models.get_file_path)),
                ('other_items', models.CharField(max_length=200, null=True)),
                ('active', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('assigned_to', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=150, null=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='view_password',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('generate_date', models.CharField(max_length=20, null=True)),
                ('view_password', models.CharField(max_length=200, null=True)),
                ('mail', models.CharField(max_length=220, null=True)),
                ('comments', models.CharField(max_length=220, null=True)),
                ('user', models.ForeignKey(to='audit.User_entry', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='weekly_audit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to='audit.User_entry', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='weekly_entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateField(null=True)),
                ('boot_time', models.CharField(max_length=20, null=True)),
                ('unused_program', models.CharField(max_length=20, null=True)),
                ('temp_file', models.CharField(max_length=20, null=True)),
                ('up_antivirus', models.CharField(max_length=20, null=True)),
                ('history_clean', models.CharField(max_length=20, null=True)),
                ('server_folder', models.CharField(max_length=20, null=True)),
                ('internet_conn', models.CharField(max_length=20, null=True)),
                ('head_phone', models.CharField(max_length=20, null=True)),
                ('depart_name', models.CharField(max_length=20, null=True)),
                ('use_system', models.CharField(max_length=20, null=True)),
                ('email_configure', models.CharField(max_length=220, null=True)),
                ('printer_conn', models.CharField(max_length=20, null=True)),
                ('issue_any', models.CharField(max_length=220, null=True)),
                ('other_items', models.CharField(max_length=200, null=True)),
                ('assigned_to', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(to='audit.User_entry', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='weekly_name_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('week_name', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='system_problem_details',
            name='user',
            field=models.ForeignKey(to='audit.User_entry', null=True),
        ),
        migrations.AddField(
            model_name='remainder_details',
            name='user',
            field=models.ForeignKey(to='audit.User_entry', null=True),
        ),
        migrations.AddField(
            model_name='register_details',
            name='user',
            field=models.ForeignKey(to='audit.User_entry', null=True),
        ),
        migrations.AddField(
            model_name='notification_details',
            name='plans',
            field=models.ForeignKey(to='audit.plan_details', null=True),
        ),
    ]
