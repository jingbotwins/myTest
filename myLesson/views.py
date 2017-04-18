#from rest_framework.decorators import api_view
#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from django.http import HttpResponse,JsonResponse
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework import status
#from rest_framework import mixins
# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.contrib.auth.models import User
from myLesson.models import MyLesson
from myLesson.serializers import MyLessonSerializer,UserSerializer
from myLesson.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users':reverse('user-list',request=request,format=format),
        'myLesson':reverse('myLesson-list',request=request,format=format)
    })

class MyLessonHighlight(generics.GenericAPIView):
    queryset = MyLesson.objects.all()
    serializer_class = MyLessonSerializer
    renderer_classes = (renderers.StaticHTMLRenderer,)
    def get(self,request,*args,**kwargs):
        myLesson = self.get_object()
        return Response(myLesson.highlighted)

class MyLessonList(generics.ListCreateAPIView):
    queryset = MyLesson.objects.all()
    serializer_class = MyLessonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class MyLessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyLesson.objects.all()
    serializer_class = MyLessonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





'''
class MyLessonList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = MyLesson.objects.all()
    serializer_class = MyLessonSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class MyLessonDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = MyLesson.objects.all()
    serializer_class = MyLessonSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

        
class MyLessonList(APIView):
    """
    List all myLesson, or create a new myLesson.
    """
    def get(self,request,format=None):
        myLesson = MyLesson.objects.all()
        serializer = MyLessonSerializer(myLesson,many=True)
        return Response(serializer.data)

    def post(self,reuqest,format=None):
        serializer = Myserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,stauts=status.HTTP_400_BAD_REQUEST)

class MyLessonDetail(APIView):
    """
    Retrieve,update or delete a myLesson instance.
    """
    def get_object(self,pk):
        try:
            return MyLesson.objects.get(pk=pk)
        except MyLesson.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        myLesson = self.get_object(pk)
        serializer = MyLessonSerializer(myLesson)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        myLesson = self.get_object(pk)
        serializer = MyLessonSerializer(myLesson,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        myLesson = self.get_object(pk)
        myLesson.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def MyLesson_list(request,format=None):
    """
    List all MyLesson,or create a new MyLesson    
    """
    if request.method == 'GET':
        myLesson = MyLesson.objects.all()
        serializer = MyLessonSerializer(myLesson,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MyLessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def MyLesson_detail(request,pk,format=None):
    """
    Retrieve,update or delete a myLesson instance
    """
    try:
        myLesson = MyLesson.objects.get(pk=pk)
    except MyLesson.DoesNotExit:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MyLessonSerializer(myLesson)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MyLessonSerializer(myLesson,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        myLesson.detele()
        return Response(status=status.HTTP_204_NO_CONTENT)


def MyLesson_list(request):
    if request.method == 'GET':
        myLesson = MyLesson.objects.all()
        serializer = MyLessonSerializer(myLesson,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(reuqest)
        serializer = MyLessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

def MyLesson_detail(request,pk):
    """
    Retrieve,update or delete a code MyLesson
    """
    try:
        myLesson = MyLesson.objects.get(pk=pk)
    except MyLesson.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MyLessonSerializer(myLesson)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MyLessonSerializer(myLesson,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        myLesson.delete()
        return HttpResponse(status=204)
    

'''
