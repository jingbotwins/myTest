from django.conf.urls import url,include
from myLesson import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',views.api_root),
    url(r'^users/$',views.UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
	url(r'^myLesson/$',views.MyLessonList.as_view(),name='myLesson-list'),
	url(r'^myLesson/(?P<pk>[0-9]+)/$',views.MyLessonDetail.as_view(),name='myLesson-detail'),
    url(r'^myLesson/(?P<pk>[0-9]+)/highlight/$',views.MyLessonHighlight.as_view(),name='myLesson-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


