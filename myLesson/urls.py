'''
from django.conf.urls import url,include
from myLesson.views import MyLessonViewSet,UserViewSet,api_root
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

myLesson_list = MyLessonViewSet.as_view({
    'get':'list',
    'post':'create'
})

myLesson_detail = MyLessonViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

myLesson_highlight = MyLessonViewSet.as_view({
    'get':'highlight'
},renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get':'list'
})
user_detail = UserViewSet.as_view({
    'get':'retrieve'
})


urlpatterns = [
    url(r'^$',api_root),
    url(r'^users/$',user_list,name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',user_detail,name='user-detail'),
	url(r'^myLesson/$',myLesson_list,name='myLesson-list'),
	url(r'^myLesson/(?P<pk>[0-9]+)/$',myLesson_detail,name='myLesson-detail'),
    url(r'^myLesson/(?P<pk>[0-9]+)/highlight/$',myLesson_highlight,name='myLesson-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
'''
