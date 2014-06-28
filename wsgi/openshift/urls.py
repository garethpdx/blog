from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


handler404 = 'openshift.views.go404'


urlpatterns = patterns('',
                       url(r'^$', 'openshift.views.index', name='home'),
                       url(r'^blog/$', 'openshift.views.index'),
                       #  A post using the blob
                       url(r'^(\d{4})/(\d{1,2})/(?P<post_name>[a-zA-Z0-9-_]{1,40})/$',
                           'openshift.views.post'),
                       # Link to posting a comment
                       url(r'^(\d{4})/(\d{1,2})/(?P<post_name>[a-zA-Z0-9-_]{1,40})/comment/$', 'openshift.views.comment'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^robots.txt$',
                           lambda x: HttpResponse("User-agent: *\nDisallow: ",
                                                  mimetype="text/plain")),
                       # The old url format
                       url(r'^blog/(?P<post_id>\d+)/$',
                           'openshift.views.redirect_old_url'),
                       url(r'^blog/(?P<post_id>\d+)/comment/$',
                           'openshift.views.comment'),
                       url(r'^blog/comment/$',
                           'openshift.views.comment'),
                       url(r'^measurement/(?P<username>[a-z]{1,10})/$',
                       #  url(r'^measurement/gareth/$',
                           'openshift.views.measure')
                       )
# url(r'^openshift/', include('openshift.foo.urls')),
# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
# Uncomment the next line to enable the admin:
