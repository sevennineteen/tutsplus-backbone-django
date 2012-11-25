from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Custom apps URLs:
    (r'^contacts/', include('bbtuts.contacts.urls')),
    (r'^$', 'bbtuts.contacts.views.home'),

)
