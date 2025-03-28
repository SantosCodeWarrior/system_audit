from django.shortcuts import render
from django.shortcuts import render,render_to_response
from audit import models
from django.http import HttpResponse
import json
from django.db.models import Count
from django.db import connection
from datetime import date,timedelta,datetime
from collections import Counter
import numpy as np
import decimal
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import os
import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import requests
import calendar


def dashboard(request):
	print 'dddddddddddd'
	return render_to_response("base.html",{})


def asset_registers(request):
	asset_details = models.asset_registers.objects.all()
	asset_array = []
	for x in asset_details:
		asset_array.append({
			'id' 				: x.id,
			'asset_name'        : x.asset_name,			
			'asset_type'		: x.asset_type,
			'state'				: x.state,
			'date_purchase'		: str(x.date_purchase),
			'expiry_date'		: str(x.expiry_date),
			'company'			: x.company,
			'serial_no'			: x.serial_no,
			'remark'			: x.remark,
			'assigned_to'		: x.assigned_to,
			'register_date'		: str(x.register_date),
			'particular' 		: x.particular,
			})
	context={
	'asset_array' : asset_array
	}
		
	return render_to_response("audit_display/asset_list.html",context)



def submit_register(request):
	e_asset_name	 = json.loads(request.GET['e_asset_name'])
	e_asset_type	 = json.loads(request.GET['e_asset_type'])
	e_state		 	 = json.loads(request.GET['e_state'])
	e_date_purchase	 = json.loads(request.GET['e_date_purchase'])
	e_expiry_date	 = json.loads(request.GET['e_expiry_date'])
	e_company		 = json.loads(request.GET['e_company'])
	e_serial_no		 = json.loads(request.GET['e_serial_no'])
	e_remark		 = json.loads(request.GET['e_remark'])	
	e_assigned_to    = json.loads(request.GET['e_assigned_to'])


	check = models.asset_registers.objects.filter(assigned_to=e_assigned_to).count()
	
	if check==1:
		save_db = models.asset_registers.objects.filter(assigned_to=e_assigned_to).first()
		msg = 'no'
	else:
		save_db = models.asset_registers()
		msg  = 'done'
	save_db.asset_name	  = e_asset_name	 
	save_db.asset_type	  = e_asset_type	 
	save_db.state		  = e_state		 	
	save_db.date_purchase = e_date_purchase
	save_db.expiry_date   = e_expiry_date	 
	save_db.company		  = e_company		
	save_db.serial_no	  = e_serial_no		
	save_db.remark		  = e_remark
	save_db.assigned_to   = e_assigned_to
	save_db.register_date = datetime.now().date()	
	save_db.save()	
	return HttpResponse(json.dumps(msg))


def update_register(request):
	ex_assetID   		= json.loads(request.GET['ex_assetID'])
	ex_asset_name   	= json.loads(request.GET['ex_asset_name'])
	ex_asset_type   	= json.loads(request.GET['ex_asset_type'])
	ex_state  			= json.loads(request.GET['ex_state'])
	ex_purchase_date   	= json.loads(request.GET['ex_purchase_date'])
	ex_expiry_date   	= json.loads(request.GET['ex_expiry_date'])
	ex_company   		= json.loads(request.GET['ex_company'])
	ex_serial_no   		= json.loads(request.GET['ex_serial_no'])
	ex_remarks   		= json.loads(request.GET['ex_remarks'])
	ex_assigned_to   	= json.loads(request.GET['ex_assigned_to'])
	ex_particular	    = json.loads(request.GET['ex_particular'])

	update_db = models.asset_registers.objects.filter(id=ex_assetID).first()
	update_db.asset_name	= ex_asset_name	
	update_db.asset_type	= ex_asset_type
	update_db.state			= ex_state
	update_db.particular    = ex_particular


	if ex_purchase_date:
		update_db.date_purchase	= ex_purchase_date
	else:
		update_db.date_purchase	= None

	if ex_expiry_date:
		update_db.expiry_date	= ex_expiry_date
	else:
		update_db.expiry_date	= None
	update_db.company		= ex_company
	update_db.serial_no		= ex_serial_no
	update_db.remark		= ex_remarks
	update_db.assigned_to	= ex_assigned_to
	update_db.save()
	return HttpResponse(json.dumps('done'))