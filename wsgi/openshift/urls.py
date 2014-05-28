from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView
from django.conf.urls.defaults import handler404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'openshift.views.go404'

urlpatterns = patterns('',
                       url(r'^$', 'openshift.views.index', name='home'),
                       url(r'^blog/$', 'openshift.views.index'),
                       url(r'^blog/(?P<post_id>\d+)/$',
                           'openshift.views.post'),
                       url(r'^blog/(?P<post_id>\d+)/comment/$',
                           'openshift.views.comment'),
                       url(r'^blog/comment/$',
                           'openshift.views.comment'),
                       url(r'^admin/', include(admin.site.urls)),
					   # Hard code 301-redirects until I figure out how to map all of the redirects.
					   url(r'.*upgrading-sql-server-2012-from.html',RedirectView.as_view(url='/blog/10/')),
					   url(r'.*connecting-to-sql-server-from-sikuli.html',RedirectView.as_view(url='/blog/8/')),
					   
					   )

					   
# url(r'^openshift/', include('openshift.foo.urls')),
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# Uncomment the next line to enable the admin:
