from rest_framework import serializers
from myLesson.models import MyLesson
from django.contrib.auth.models import User

class MyLessonSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
 #   url = serializers.HyperlinkedIdentityField(view_name="MyLesson-detail")
#    highlight = serializers.HyperlinkedIdentityField(view_name='myLesson_highlight',format='html')
    class Meta:
        model = MyLesson
        #fields = ('url','id','owner','highlight','title','code','linenos','language','style')
        fields = ('url','id','owner','title','code','linenos','language','style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
#    myLesson = serializers.PrimaryKeyRelatedField(many=True,queryset=MyLesson.objects.all())
#    url = serializers.HyperlinkedIdentityField(view_name="user-detail")
#    myLesson = serializers.HyperlinkedRelatedField(many=True,view_name='MyLesson-detail',read_only=True)
    class Meta:
        model = User
        fields = ('url','id','username','myLesson')


'''
class MyLessonSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False,allow_blank=True,max_length=100)
	code = serializers.CharField(style={'base_template':'textarea.html'})
	linenous = serializers.BooleanField(required=False)
	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
	style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')

	def created(self, validated_data):
		"""
		Create and return a new 'MyLesson' instance, given the validated data.
		"""
		return MyLesson.objects.create(**validated_data)

	def update(self,instance,validated_data):
		"""
		Update and return an existing 'MyLesson' instance, given the validated data.
		"""
		instance.title = validated_data.get('title',instance.title)
		instance.code = validated_data.get('code',instance.code)
		instance.linenos = validated_data.get('linenos',instance.linenos)
		instance.language = validated_data.get('language',instance.language)
		instance.style = validated_data.get('style',instance.style)
		instance.save()
		return instance
'''


