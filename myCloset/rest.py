from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from myCloset import classBasedAPI

urlpatterns = patterns('',
    url(r'^brands/$', classBasedAPI.BrandList.as_view()),
    url(r'^apparels/$', classBasedAPI.ApparelList.as_view()),
    url(r'^cloths/$', classBasedAPI.ClothList.as_view()),
    url(r'^shoes/$', classBasedAPI.ShoesList.as_view()),
    url(r'^categories/$', classBasedAPI.CategoryList.as_view()),
    url(r'^userprofiles/$', classBasedAPI.UserProfileList.as_view()),
    url(r'^users/$', classBasedAPI.UserList.as_view()),
    url(r'^brands/(?P<pk>[0-9]+)/$', classBasedAPI.BrandDetail.as_view()),
    url(r'^apparels/(?P<pk>[0-9]+)/$', classBasedAPI.ApparelDetail.as_view()),
    url(r'^cloths/(?P<pk>[0-9]+)/$', classBasedAPI.ClothDetail.as_view()),
    url(r'^shoes/(?P<pk>[0-9]+)/$', classBasedAPI.ShoesDetail.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', classBasedAPI.CategoryDetail.as_view()),
    url(r'^userprofiles/(?P<pk>[0-9]+)/$', classBasedAPI.UserProfileDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', classBasedAPI.UserInstance.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)