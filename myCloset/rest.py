from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from myCloset import classBasedAPI

urlpatterns = patterns('',
#===============================================================================
# lists
#===============================================================================
    url(r'^brands/$', classBasedAPI.BrandList.as_view()),
    url(r'^apparelType/$', classBasedAPI.ApparelTypeList.as_view()),
    url(r'^clothsType/$', classBasedAPI.ClothTypeList.as_view()),
    url(r'^shoesType/$', classBasedAPI.ShoesTypeList.as_view()),
    url(r'^apparelInstance/$', classBasedAPI.ApparelInstanceList.as_view()),
    url(r'^categories/$', classBasedAPI.CategoryList.as_view()),
    url(r'^userprofiles/$', classBasedAPI.UserProfileList.as_view()),
    url(r'^users/$', classBasedAPI.UserList.as_view()),
    url(r'^locations/$', classBasedAPI.LocationList.as_view()),
    
    
#===============================================================================
# individuals
#===============================================================================
    url(r'^brands/(?P<pk>[0-9]+)/$', classBasedAPI.BrandDetail.as_view()),
    url(r'^apparelType/(?P<pk>[0-9]+)/$', classBasedAPI.ApparelTypeDetail.as_view()),
    url(r'^apparelInstance/(?P<pk>[0-9]+)/$', classBasedAPI.ApparelInstanceDetail.as_view()),
    url(r'^cloths/(?P<pk>[0-9]+)/$', classBasedAPI.ClothDetail.as_view()),
    url(r'^shoes/(?P<pk>[0-9]+)/$', classBasedAPI.ShoesDetail.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', classBasedAPI.CategoryDetail.as_view()),
    url(r'^userprofiles/(?P<pk>[0-9]+)/$', classBasedAPI.UserProfileDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', classBasedAPI.UserInstance.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', classBasedAPI.LocationDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)