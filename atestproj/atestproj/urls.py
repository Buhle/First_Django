from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atestproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'contact_app.views.home', name='home'),

	url(r'^contacts$', 'contact_app.views.contact_list', name='contact_list'),

	url(r'^template$', 'contact_app.views.test_template', name='template'),

	url(r'^index$', 'contact_app.views.index', name='index'),


)
