from django.db import models
import os
from django.core.files import File
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings

def get_file_path(instance, filename):
	ext       		= filename.split('.')[-1]
	my_id 	  		= uuid.uuid1()
	encry     		= my_id
	filename  		= "%s.%s" % (""+str(encry), ext)
	return os.path.join('/audit/static/bill/', filename)


class User_entry(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	user_name 		= models.CharField(max_length = 200, null = True)
	processor 		= models.CharField(max_length = 200, null = True)
	ram 		    = models.CharField(max_length = 200, null = True)
	hdd  		    = models.CharField(max_length = 200, null = True)
	keyboard	    = models.CharField(max_length = 200, null = True)
	mouse	   		= models.CharField(max_length = 200, null = True)
	smps	        = models.CharField(max_length = 200, null = True)
	monitor	        = models.CharField(max_length = 200, null = True)
	operating_sys   = models.CharField(max_length = 200, null = True)
	remark 		    = models.CharField(max_length = 200, null = True)
	current_date 	= models.DateField(null=True)	
	items 			= models.FileField(upload_to=get_file_path,null=True)
	other_items	    = models.CharField(max_length = 200, null = True)
	active 			= models.IntegerField(null = True)
	status 			= models.IntegerField(null = True)
	location	    = models.CharField(max_length = 200, null = True)
	assigned_to	    = models.CharField(max_length = 200, null = True)
	date_purchase	= models.DateField(null=True)
	
class weekly_entry(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	entry_date 		= models.DateField(null=True)
	user    		= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)
	boot_time 		= models.CharField(max_length = 20, null = True)
	unused_program	= models.CharField(max_length = 20, null = True)
	temp_file   	= models.CharField(max_length = 20, null = True)
	up_antivirus    = models.CharField(max_length = 20, null = True)
	history_clean   = models.CharField(max_length = 20, null = True)
	server_folder   = models.CharField(max_length = 20, null = True)
	internet_conn   = models.CharField(max_length = 20, null = True)
	head_phone      = models.CharField(max_length = 20, null = True)
	depart_name     = models.CharField(max_length = 20, null = True)
	use_system      = models.CharField(max_length = 20, null = True)
	email_configure = models.CharField(max_length = 220, null = True)
	printer_conn    = models.CharField(max_length = 20, null = True)
	issue_any       = models.CharField(max_length = 220, null = True)
	other_items	    = models.CharField(max_length = 200, null = True)
	assigned_to	    = models.CharField(max_length = 200, null = True)
	office365 	    = models.CharField(max_length = 200, null = True)

class email_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	email_user_name		= models.CharField(max_length = 200, null = True)
	

class remainder_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	remainder_date 			= models.DateField(null=True)
	user    				= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)
	office_period_date 		= models.CharField(max_length = 20, null = True)
	email_move_date			= models.CharField(max_length = 20, null = True)
	remarks					= models.CharField(max_length = 20, null = True)
	user_name 		  		= models.CharField(max_length = 200, null = True)

class register_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	register_date 	= models.DateField(null=True)
	user    		= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)
	it_non          = models.CharField(max_length = 20, null = True)
	fitting			= models.CharField(max_length = 20, null = True)
	description     = models.CharField(max_length = 20, null = True)
	location        = models.CharField(max_length = 20, null = True)
	user_allotted   = models.CharField(max_length = 20, null = True)
	security_level  = models.CharField(max_length = 20, null = True)
	maintenance     = models.CharField(max_length = 20, null = True)
	record_date		= models.DateField(null=True)
	remarks			= models.CharField(max_length = 20, null = True)	
	audit_key  		= models.CharField(max_length=100,null=True)


class network_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	action_date 			= models.DateField(null=True)	
	break_down         		= models.DateTimeField(null=True)
	name_mc					= models.CharField(max_length = 120, null = True)
	reported_name     		= models.CharField(max_length = 120, null = True)
	network_operator   	 	= models.CharField(max_length = 120, null = True)
	problem_reported   		= models.CharField(max_length = 120, null = True)
	action_taken  			= models.CharField(max_length = 120, null = True)
	time_status     		= models.DateTimeField(null=True)	
	total_time_break_down	= models.CharField(max_length = 120, null = True)
	internet_speed			= models.CharField(max_length = 120, null = True)	
	remarks  				= models.CharField(max_length=200,null=True)

class system_problem_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	called_date 		= models.DateField(null=True)	
	party_name         	= models.CharField(max_length = 220, null = True)
	party_contact      	= models.CharField(max_length = 220, null = True)
	mechanic_name		= models.CharField(max_length = 220, null = True)
	mechanic_number    	= models.CharField(max_length = 220, null = True)
	problems   		  	= models.CharField(max_length = 220, null = True)
	remarks  			= models.CharField(max_length=200,null=True)
	user    			= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)


class asset_registers(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	register_date 		= models.DateField(null=True)	
	asset_name       	= models.CharField(max_length = 220, null = True)
	asset_type      	= models.CharField(max_length = 220, null = True)
	state				= models.CharField(max_length = 220, null = True)
	date_purchase    	= models.CharField(max_length = 220, null = True)
	expiry_date   		= models.CharField(max_length = 220, null = True)
	company  			= models.CharField(max_length=200,null=True)
	remark  			= models.CharField(max_length=220,null=True)
	assigned_to			= models.CharField(max_length=200,null=True)
	count  			    = models.CharField(max_length=200,null=True)
	serial_no      		= models.CharField(max_length = 220, null = True)
	particular      	= models.CharField(max_length = 220, null = True)

class weekly_name_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	week_name  			= models.CharField(max_length=200,null=True)
	date  				= models.CharField(max_length=20,null=True)
	
class Users(models.Model):
	user 			= models.OneToOneField(User, null = True)	
	user_type 		= models.CharField(max_length = 150, null = True)


class view_password(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	user    		= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)
	generate_date 	= models.CharField(max_length=20,null=True)
	view_password	= models.CharField(max_length=200,null=True)
	mail      		= models.CharField(max_length = 220, null = True)
	comments      	= models.CharField(max_length = 220, null = True)

class weekly_audit(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	user    		= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)

class emergency_contact(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	user_name 			= models.CharField(max_length = 220, null = True)
	contact_mobile    	= models.CharField(max_length = 220, null = True)
	contact_landline   	= models.CharField(max_length = 220, null = True)
	address				= models.CharField(max_length = 220, null = True)
	remarks    			= models.CharField(max_length = 220, null = True)
	department 			= models.CharField(max_length = 220, null = True)
	entry_date  		= models.CharField(max_length = 220, null = True)

class equipment_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	category 			= models.CharField(max_length = 100, null = True)	
	label 			    = models.CharField(max_length = 100, null = True)	
	active 				= models.IntegerField(null = True)	
	brand 			    = models.CharField(max_length = 200, null = True)
	purchase_date		= models.DateField(null=True)
	stock 				= models.IntegerField(null = True)
	issue_any  			= models.CharField(max_length = 220, null = True)
	party_name			= models.CharField(max_length = 100, null = True)
	party_contact		= models.CharField(max_length = 100, null = True)
	repaired_date 		= models.DateField(null=True)
	mechanic_name 		= models.CharField(max_length = 200, null = True)
	mechanic_contact	= models.CharField(max_length = 100, null = True)
	remarks  			= models.CharField(max_length = 220, null = True)
	status 			    = models.CharField(max_length = 200, null = True)
	issue_date 			= models.DateField(null=True)


class system_wfh(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	category 			= models.CharField(max_length = 100, null = True)	
	remarks  			= models.CharField(max_length = 220, null = True)	
	issue_date 			= models.DateField(null=True)
	receive_date 		= models.DateField(null=True)
	user_name 			= models.CharField(max_length = 220, null = True)	
	cpu 				= models.CharField(max_length = 220, null = True)
	keyboard 			= models.CharField(max_length = 220, null = True)
	ups 				= models.CharField(max_length = 220, null = True)
	monitor 			= models.CharField(max_length = 220, null = True)
	headphone  		    = models.CharField(max_length = 220, null = True)
	mouse 				= models.CharField(max_length = 220, null = True)
	department 		    = models.CharField(max_length = 220, null = True)
	hdmi_cable 		    = models.CharField(max_length = 220, null = True)


class plan_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	plan_type 			= models.CharField(max_length = 220, null = True)

class notification_details(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)
	alert_date 			= models.DateField(null=True)
	email_name			= models.CharField(max_length = 220, null = True)	
	sent_date 			= models.DateField(null=True)	
	amount 				= models.CharField(max_length = 220, null = True)	
	payment_status		= models.CharField(max_length = 220, null = True)
	plans    			= models.ForeignKey(plan_details, null=True ,on_delete=models.CASCADE)
	remarks 			= models.CharField(max_length = 220, null = True)
	status 			    = models.CharField(max_length = 520, null = True)
	doc_link		    = models.CharField(max_length = 520, null = True)


class inventory_list(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	particulars 		= models.CharField(max_length = 220, null = True)	
	department 			= models.CharField(max_length = 220, null = True)
	repaired_date 		= models.DateField(null=True)
	purchase_date 		= models.DateField(null=True)
	assigned_date 		= models.DateField(null=True)
	assigned_to 		= models.CharField(max_length = 220, null = True)	
	status 				= models.CharField(max_length = 220, null = True)	
	warranty 			= models.CharField(max_length = 220, null = True)	
	brand_name 			= models.CharField(max_length = 220, null = True)	
	location 			= models.CharField(max_length = 220, null = True)	
	remarks 			= models.CharField(max_length = 220, null = True)
	entry_date 			= models.DateTimeField(default=datetime.now,blank=True)	


class monthly_tracker(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	billing_date 		= models.DateField(null=True)
	service_provider 	= models.CharField(max_length = 220, null = True)
	staff_member 		= models.CharField(max_length = 220, null = True)
	bill_no 		 	= models.CharField(max_length = 220, null = True)
	nature_expense 		= models.CharField(max_length = 220, null = True)
	amount_usd 			= models.FloatField(null=True)
	amount_sgd 			= models.FloatField(null=True)
	amount_euro 		= models.FloatField(null=True)	
	amount_inr 			= models.FloatField(null=True)	
	total 				= models.FloatField(null=True)
	remarks 			= models.CharField(max_length = 220, null = True)
	taxable				= models.FloatField(null=True)
	entry_date 			= models.DateTimeField(default=datetime.now,blank=True)	

class gst_bills_tracker(models.Model):
	def __unicode__(self):
		return '%s' % (self.id)	
	billing_date 		= models.DateField(null=True)
	service_provider 	= models.CharField(max_length = 220, null = True)	
	bill_no 		 	= models.CharField(max_length = 220, null = True)
	nature_expense 		= models.CharField(max_length = 220, null = True)
	amount_usd 			= models.FloatField(null=True)
	amount_sgd 			= models.FloatField(null=True)
	amount_euro 		= models.FloatField(null=True)	
	amount_inr 			= models.FloatField(null=True)	
	total 				= models.FloatField(null=True)
	remarks 			= models.CharField(max_length = 220, null = True)
	taxable				= models.FloatField(null=True)
	entry_date 			= models.DateTimeField(default=datetime.now,blank=True)
	user    			= models.ForeignKey(User_entry, null=True ,on_delete=models.CASCADE)
	warranty_time  		= models.FloatField(null=True)