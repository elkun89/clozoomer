from django.conf.urls import patterns, include, url
from myCloset import views

urlpatterns = patterns('',
    url(r'^getApparelType/(?P<idNum>\d+)/$', views.getApparelType, name  = 'getApparelType'),
    url(r'^categories/$', views.listCategoryByJson, name  = 'listCategoryByJson'),
    url(r'^userProfile/$', views.requestUserProfile, name  = 'requestUserProfile'),
    url(r'^randomTest/$', views.randomTest, name  = 'randomTest'),
    url(r'^getFriends/$', views.getFriends, name  = 'randomTest'),
    url(r'^getProfile/$', views.getProfile, name  = 'getProfile'),
    url(r'^editProfile/$', views.editProfile, name  = 'editProfile'),
    url(r'^newPost/$', views.createPost, name  = 'newPost'),
    url(r'^getPosts/$', views.showPosts, name  = 'getPosts'),
    url(r'^getCloset/$', views.displayCloset, name  = 'getCloset'),
    url(r'^addApparelInstance/$', views.add_apparel_instance, name = 'add_apparel_instance'),
    url(r'^deleteApparelInstance/(?P<idNum>\d+)/$', views.delete_apparel_instance, name  = 'delete_apparel_instance'),
    url(r'^deletePost/(?P<idNum>\d+)/$', views.delete_post, name = 'delete_post'),
    url(r'^requestFriend/$', views.add_friend_request, name = 'add_friend_request'),
    url(r'^showFriendRequest/$', views.show_friend_request, name = 'show_friend_request'),
    url(r'^processFriendRequest/$', views.process_friend_request, name = 'process_friend_request'),
    url(r'^listApparelInstance/$', views.listApparel, name = 'listApparel'),
    url(r'^search/$', views.basic_search, name = 'search')
)

