from django.conf.urls import url
from myLesson import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^myLesson/$',views.MyLesson_list),
	url(r'^myLesson/(?P<pk>[0-9]+)/$',views.MyLesson_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)


