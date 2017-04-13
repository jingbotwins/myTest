from django.conf.urls import url
from myLesson import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^myLesson/$',views.MyLessonList.as_view()),
	url(r'^myLesson/(?P<pk>[0-9]+)/$',views.MyLessonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


