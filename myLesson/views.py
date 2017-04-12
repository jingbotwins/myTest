from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from myLesson.models import MyLesson
from myLesson.serializers import MyLessonSerializer

# Create your views here.

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
    


