"""myTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include,patterns
from myLesson import views
from rest_framework.routers import DefaultRouter


#creatw a router and register our viewsets with it
router = DefaultRouter()
router.register(r'myLesson',views.MyLessonViewSet)
router.register(r'users',views.UserViewSet)

#The API URLs are now determined automatically by the router.
#Additionly, we include the login URLs for browsable API
urlpatterns = patterns('',
    url(r'^',include(router.urls)),
    url(r'^api_auth/',include('rest_framework.urls',namespace='rest_framework'))
)
'''
from django.conf.urls import url,include
from myLesson import views
from rest_framework.routers import DefaultRouter
#from django.contrib import admin
#from django.contrib.auth.models import User,Group
#fprom rest_framework import routers,serializers,viewsets

#Create a router and register our viewsets with it.
#router = DefaultRouter()
#router.register(r'myLesson',views.MyLessonViewSet)
#router.register(r'users',views.UserViewSet)

#The API URLs are now determined automatically by the router.
#Additionally, we include login URLs for the browsable API
urlpatterns = [
    #url(r'^',include(router.urls)),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	url(r'^',include('myLesson.urls')),
]


#Serializer define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url','username','email','is_staff','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url','name')

#ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	
#Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'groups',GroupViewSet)
'''

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#}
