from django.conf.urls import patterns, include, url
from myCloset import views

urlpatterns = patterns('',
    url(r'^apparel/$', views.listApparelByJson, name  = 'listApparelByJson'),
    url(r'^randomTest/$', views.randomTest, name  = 'randomTest'),
)

