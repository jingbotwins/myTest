from django.conf.urls import url
from myLesson import views

urlpatterns = [
	url(r'^myLesson/$',views.MyLesson_list),
	url(r'^myLesson/(?P<pk>[0-9]+)/$',views.MyLesson_detail),
]
