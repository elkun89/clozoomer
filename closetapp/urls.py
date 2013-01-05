from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from myCloset import views
import myCloset

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'closetapp.views.home', name='home'),
    # url(r'^closetapp/', include('closetapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.landing, name = 'landing'),
    url(r'^', include('myCloset.urls')),
    url(r'^rest/', include('myCloset.rest')),
    url(r'^accounts/register', views.register, name = 'register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
    {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
    {'template_name': 'logged_off.html'}),
)
