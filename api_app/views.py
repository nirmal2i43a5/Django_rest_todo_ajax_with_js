from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
	}
    
    return Response(api_urls)


    
    # return JsonResponse("I am json file",safe=False)
   
@api_view(['GET'])
def taskList(request):
    
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)#serializing tasks data ->many = True means serilizing list 
    #second paramater signifies do we want to serializers one object or list 
    
    return Response(serializer.data)#serializer data and return in api response


@api_view(['GET'])
def taskDetail(request, tid):#to see for particular id details
	tasks = get_object_or_404(Task,pk=tid)
	serializer = TaskSerializer(tasks, many=False)#we use one one object so many = False
	return Response(serializer.data)



@api_view(['POST'])
def taskCreate(request):#we send post data
	serializer = TaskSerializer(data=request.data)#in models forms we do request.POST in restful ---request.data return json object
	print(f'--------------{serializer}--------------------')

	if serializer.is_valid():#in restful we save form and is sililar concept
		serializer.save()

	return Response(serializer.data)



@api_view(['POST'])
def taskUpdate(request, tid):
	task =  get_object_or_404(Task,pk=tid)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()
  
	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, tid):
	task = get_object_or_404(Task,pk=tid)
	task.delete()

	return Response('Item succsesfully delete!')