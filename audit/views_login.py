import django.middleware.csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from audit import models
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib import messages
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.models import User
from ipware.ip import get_ip
# import grequests
from django.conf import settings
import urllib
import urllib2


@csrf_exempt
def user_login(request):
	if request.method == 'POST':		
		username = json.loads(request.POST['username'])
		password = json.loads(request.POST['password'])		
		user 	 = authenticate(username = username, password = password)
		
		if user and models.Users.objects.filter(user=user).first().user_type=='admin':
			if user.is_active:				
				login(request,user)				
				# try:
				# 	ip_detail=get_user_ip(request)
				# 	save_ip_det(ip_detail,user.id,username)
				# except:
				# 	pass
				return HttpResponse(json.dumps('loggedin'))
			else:
				return HttpResponse(json.dumps("account disabled"))
		else:
			return HttpResponse(json.dumps("invalid"))
		# else:
		# 	return HttpResponse(json.dumps("invalid"))
	else:		
		if request.user.is_authenticated() and models.Users.objects.filter(user = request.user)[0].user_type == 'admin':			
			return HttpResponseRedirect('/audit/welcome')
		return render_to_response('login/login.html',  RequestContext(request, {}))


@csrf_exempt
def user_entryx(request):
	if request.method == 'POST':
		user_data = (request.POST)
		if True:
			un 		= user_data['username']
			ps 		= user_data['password']
			email 	= user_data['email']
			user 	= User.objects.create_user(username=un,email=email,password=ps)
			#print '_______',user
			user_model = models.Users()
			user_model.user = user
			user_model.user_type = user_data['user_type']
			# if user_data['user_type'] == 'client':
			# 	client = models.Client.objects.filter(id = user_data['obj_id'])[0]
			# 	user_model.client = client
			# else:
			# 	voyage_manager = models.Voyage_Manager.objects.filter(id = user_data['obj_id'])[0]
			# 	user_model.voyage_manager = voyage_manager
			user_model.save()
			return HttpResponse(json.dumps('done'))
		else:
			return HttpResponse(errors)
	else:
		return render(request,'login/data_entry_user.html', {})
	# else:
	# 	#return render(request,'login/data_entry_users.html', {})
	# 	return HttpResponseRedirect('/hb/user_login')

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/audit/user_login')

# def usertype_selecthandler(request):
# 	# if request.user.is_authenticated() and models.Users.objects.filter(user = request.user)[0].user_type == 'admin':
# 	if True:
# 		data=json.loads(request.GET['client_type'])
# 		if data=='1':
# 			list2=list(models.Client.objects.values_list('id','client_name').all())

# 		elif data=='2':
# 			list2=list(models.Pool.objects.values_list('id','pool_name').all())
# 		elif data=='3':
# 			list2=list(models.Voyage_Manager.objects.values_list('id','name').all())
# 		elif data=='4':
# 			list2=list(models.Ship.objects.values_list('id','ship_name').all())
# 		elif data=='5':
# 			list2=list(models.Charterer.objects.values_list('id','charterer_name').all())
# 		elif data=='6':
# 			list2=list(models.Receiver.objects.values_list('id','receiver_name').all())
# 		resp_data={}
# 		resp_data['list']=list2
# 		resp_data['type']=data
# 		list2=json.dumps(resp_data)
# 		return HttpResponse(list2)
# 	elif request.user.is_authenticated():
# 		return HttpResponseRedirect('/hb/welcome')
# 	else:
# 		return HttpResponseRedirect('/hb/user_login')


# def get_user_ip(request):
# 	try:
# 		ip = get_ip(request)
# 		#print "------------"
# 		hosts=[]
# 		if ip is not None:
# 			#print "we have an IP address for user",ip
# 			hosts.append('http://api.db-ip.com/addrinfo?addr='+str(ip)+'&api_key=fa871e8abacd62600db9f57aa5746f2e15cd0d40')
# 			#print "---------------------",hosts
# 			rs=(grequests.get(u) for u in hosts)
# 			response=grequests.map(rs)
# 			for r in response:
# 				# try:
# 				ip_detail=json.loads(r.text)
# 			return ip_detail
# 		else:
# 			return 0
# 	except:
# 		pass


# def save_ip_det(ip_detail,user_id,username):
# 	if ip_detail!=0:
# 		log 			=	 	models.login_log()
# 		log.user_id_id	=	 	user_id
# 		#print ip_detail['address']
# 		log.ip_adress	=	 	ip_detail['address']
# 		log.country 	= 	 	ip_detail['country']
# 		log.state 		= 		ip_detail['stateprov']
# 		log.city 		= 		ip_detail['city']
# 		log.save()
# 		try:
# 			send_simple_message(ip_detail['address'],username,ip_detail['city'],ip_detail['country'],ip_detail['stateprov'],str(datetime.now())[0:16])
# 		except:
# 			pass
# 	else:
# 		log 			= 		models.login_log()
# 		log.user_id_id	=		user_id
# 		log.ip_adress	=		0
# 		log.country		=		"-"
# 		log.state 		= 		"-"
# 		log.city 		= 		"-"
# 		log.save()


# def send_simple_message(ip_address,username,city,country,state,e_date):
# 	import smtplib
# 	import pprint
# 	from email.mime.multipart import MIMEMultipart
# 	from email.mime.text import MIMEText
# 	from django.core.mail import EmailMultiAlternatives
# 	from email.MIMEImage import MIMEImage
# 	try:
# 		#if ip_address!='202.91.91.101' and ip_address!='59.89.23.220' and ip_address!='139.167.6.122' and ip_address!='117.201.83.188' and ip_address!='127.0.0.1' and ip_address!='139.167.6.137' and ip_address!='139.167.10.23' and ip_address!='139.167.10.238' and ip_address!='139.167.10.74':
# 		html_content   = "Good day <b><font color='#FFD728'>Heat</font><font color='#323296'>bank</font></b>, <br/><br/> <b>"+str(username)+"</b> logged in to <b><font color='#FFD728'>Heat</font><font color='#323296'>bank</font></b> from <b>"+str(country)+"</b> , <b>"+str(state)+"</b>, <b>"+str(city)+"</b> using IP Address <b>"+str(ip_address)+"</b> on <b>"+str(e_date)+" GMT</b><br/><br/> <b>Thanks & Best Regards</b><br/>HEATBANK TEAM"
# 		mailto 		   = 'santosh@bwesglobal.com'
# 		cc_email 	   = 'santoshmessage14@gmail.com'
# 		mailsubject    = 'Login Alert from HEATBANK'
# 		text_content   = 'This is an important message.'
# 		msg 		   = EmailMultiAlternatives(mailsubject,text_content,'santosh@bwesglobal.com',[mailto],bcc=[cc_email])
# 		msg.attach_alternative(html_content, "text/html")
# 		msg.send()
# 	except:
# 		pass