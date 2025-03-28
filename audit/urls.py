from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from audit import views
from audit import asset_registor as ar
from audit import export_tracker as exp
from audit import views_login as vl
from audit import inventory_system as sys
from audit import unused_computer as uc
from audit import internet_recharge as ir
from audit import system_details as sd
from audit import system_list as sls
from audit import monthly_tracker as tt
from audit import view_bills as vbs
from audit import office_tracker as oft

urlpatterns = patterns('',	
	url(r'^dashboard/', views.dashboard, name = 'dashboard'),
	url(r'^welcome/', views.welcome, name = 'welcome'),
	url(r'^user_entry/', views.user_entry, name = 'user_entry'),

	url(r'^submit_entry/', views.submit_entry, name = 'submit_entry'),
	url(r'^entry_form/', views.entry_form, name = 'entry_form'),
	url(r'^submit_weekly_entry/', views.submit_weekly_entry, name = 'submit_weekly_entry'),
	url(r'^remainder/', views.remainder, name = 'remainder'),
	url(r'^update_key_details/', views.update_key_details, name = 'update_key_details'),
	url(r'^view_audit/', views.view_audit, name = 'view_audit'),
	url(r'^submit_remainder_entry/', views.submit_remainder_entry, name = 'submit_remainder_entry'),
	url(r'^assets_register/', views.assets_register, name = 'assets_register'),
	url(r'^submit_register_entry/', views.submit_register_entry, name = 'submit_register_entry'),
	url(r'^view_register_entry/', views.view_register_entry, name = 'view_register_entry'),
	url(r'^update_user_entry/', views.update_user_entry, name = 'update_user_entry'),

	url(r'^view_system_configuration/', views.view_system_configuration, name = 'view_system_configuration'),
	url(r'^view_user_configuration/', views.view_user_configuration, name = 'view_user_configuration'),
	url(r'^network_speed_details/', views.network_speed_details, name = 'network_speed_details'),
	url(r'^misc_details/', views.misc_details, name = 'misc_details'),
	url(r'^misc_details_entry/', views.misc_details_entry, name = 'misc_details_entry'),

	url(r'^system_log/', views.system_log, name = 'system_log'),	
	url(r'^submit_log/', views.submit_log, name = 'submit_log'),	
	url(r'^view_sys_info/', views.view_sys_info, name = 'view_sys_info'),	
	url(r'^update_sys_log/', views.update_sys_log, name = 'update_sys_log'),

	url(r'^asset_registers/', ar.asset_registers, name = 'asset_registers'),	
	url(r'^submit_register/', ar.submit_register, name = 'submit_register'),		
	url(r'^update_register/', ar.update_register, name = 'update_register'),	

	url(r'^export_tracker/', exp.export_tracker, name = 'export_tracker'),		
	url(r'^weekly_audit_export/', exp.weekly_audit_export, name = 'weekly_audit_export'),		
	url(r'^load_selected_date/', exp.load_selected_date, name = 'load_selected_date'),		
	
	url(r'^user_login/', vl.user_login, name = 'user_login'),	
	url(r'^user_logout/', vl.user_logout, name = 'user_logout'),
	url(r'^user_entryx/', vl.user_entryx, name = 'user_entryx'),		

	url(r'^selected_date_view_audit/', views.selected_date_view_audit, name = 'selected_date_view_audit'),
	url(r'^view_pwd/', views.view_pwd, name = 'view_pwd'),
	url(r'^update_pwd_details/', views.update_pwd_details, name = 'update_pwd_details'),
	url(r'^submit_pwd_details/', views.submit_pwd_details, name = 'submit_pwd_details'),

	url(r'^refresh_weekly_entry/', views.refresh_weekly_entry, name = 'refresh_weekly_entry'),
	
	#url(r'^send_mail_for_recharge/', views.send_mail_for_recharge, name = 'send_mail_for_recharge'),
	# url(r'^upload', views.get_base_upload, name = 'upload'),
	url(r'^contact_details/', views.contact_details, name = 'contact_details'),	
	url(r'^update_contact_entry/', views.update_contact_entry, name = 'update_contact_entry'),
	url(r'^submit_contact_entry/', views.submit_contact_entry, name = 'submit_contact_entry'),	
	url(r'^export_contact_details/', views.export_contact_details, name = 'export_contact_details'),	
	url(r'^contact_details_download/', views.contact_details_download, name = 'contact_details_download'),	

	url(r'^system_export/', exp.system_export, name = 'system_export'),	
	url(r'^export_system_details/', exp.export_system_details, name = 'export_system_details'),	

	url(r'^inventory_system/', sys.inventory_system, name = 'inventory_system'),
	url(r'^submit_inventory_entry/', sys.submit_inventory_entry, name = 'submit_inventory_entry'),
	url(r'^update_inventory_details/', sys.update_inventory_details, name = 'update_inventory_details'),

	url(r'^system_wfh/', sys.system_wfh, name = 'system_wfh'),
	url(r'^submit_wfh_entry/', sys.submit_wfh_entry, name = 'submit_wfh_entry'),
	#url(r'^view_wfh_entry/', sys.view_wfh_entry, name = 'view_wfh_entry'),
	url(r'^export_inventory_details/', sys.export_inventory_details, name = 'export_inventory_details'),
	url(r'^export_inventory_list/', sys.export_inventory_list, name = 'export_inventory_list'),
	
	url(r'^system_wfh_details/', sys.system_wfh_details, name = 'system_wfh_details'),
	url(r'^view_audit_summary/', uc.view_audit_summary, name = 'view_audit_summary'),

	url(r'^export_password_share/', exp.export_password_share, name = 'export_password_share'),	
	url(r'^download_password_share/', exp.download_password_share, name = 'download_password_share'),	

	url(r'^internet_recharge/', ir.internet_recharge, name = 'internet_recharge'),	
	url(r'^update_remind_entry/', ir.update_remind_entry, name = 'update_remind_entry'),	
	url(r'^insert_remind_entry/', ir.insert_remind_entry, name = 'insert_remind_entry'),
	url(r'^add_plan_entry/', ir.add_plan_entry, name = 'add_plan_entry'),
	url(r'^delete_entry/', ir.delete_entry, name = 'delete_entry'),

	url(r'^system_details/', sd.system_details, name = 'system_details'),

	url(r'^system_list/', sls.system_list, name = 'system_list'),
	url(r'^system_details_entry/', sls.system_details_entry, name = 'system_details_entry'),
	url(r'^system_details_list/', sls.system_details_list, name = 'system_details_list'),

	url(r'^get_alert_system/', views.get_alert_system, name = 'get_alert_system'),

	url(r'^get_configuration_details/', views.get_configuration_details, name = 'get_configuration_details'),
	
	url(r'^tracker/', tt.tracker, name = 'tracker'),
	url(r'^submit_tracker_entry/', tt.submit_tracker_entry, name = 'submit_tracker_entry'),
	url(r'^system_tracker_details/', tt.system_tracker_details, name = 'system_tracker_details'),

	url(r'^view_bills/', vbs.view_bills, name = 'view_bills'),
	url(r'^get_bills_details/', vbs.get_bills_details, name = 'get_bills_details'),

	url(r'^office_tracker/', oft.office_tracker, name = 'office_tracker'),
	url(r'^submit_bills_details/', vbs.submit_bills_details, name = 'submit_bills_details'),
)



