from django.conf.urls import patterns, include, url
from myCloset import views

urlpatterns = patterns('',
    url(r'^apparel/$', views.listApparelByJson, name  = 'listApparelByJson'),
    url(r'^getApparelType/(?P<idNum>\d+)/$', views.getApparelType, name  = 'getApparelType'),
    url(r'^categories/$', views.listCategoryByJson, name  = 'listCategoryByJson'),
    url(r'^userProfile/$', views.requestUserProfile, name  = 'requestUserProfile'),
    url(r'^randomTest/$', views.randomTest, name  = 'randomTest'),
    url(r'^getFriends/$', views.getFriends, name  = 'randomTest'),
    url(r'^getProfile/$', views.getProfile, name  = 'getProfile'),
)

