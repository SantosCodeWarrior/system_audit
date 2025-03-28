from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
	url(r'^$','audit.views_login.user_login', name='user_login'),
    # url(r'^$', 'audit.views.welcome', name='welcome'),    
	# url(r'^$', 'audit.views.dashboard', name='dashboard'),    
    url(r'^audit/',include('audit.urls')),
    url(r'^admin/',include(admin.site.urls)),
]+static(settings.STATIC_URL,document_root=settings.AUDIT_PATH)
