from django.conf.urls.defaults import *

urlpatterns = patterns('bbtuts.contacts.views',

	url(r'^$', 'contact_list'),
	url(r'^(?P<pk>\d+)/?$', 'contact_detail'),
)