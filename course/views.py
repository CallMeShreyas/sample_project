from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def get_course_all(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_course(request, id):
    course = Course.objects.filter(id = id)
    if course.exists():
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)
    else:
        return Response({
            "status": "failure",
            "info": "Course dose not exists"
        })


@api_view(['POST'])
def post_course(request):
    data = request.data
    serializer = CourseSerializer(data = data)
    if serializer.is_valid():
        name = data['name']
        course = Course.objects.filter(name=name)
        if course.exists():
            return Response({
                "status": "failure",
                "info": "Course Name Exists"
            })

        serializer.save()
        return Response({
            "status": "success",
            "info": "Data Saved Successfully"
        })

    else:
        return Response({
            "status": "failure",
            "info": serializer.errors
        })

@api_view(['PUT'])
def put_course(request, id):
    data = request.data
    serializer = CourseSerializer(data = data)
    if serializer.is_valid():
        course = Course.objects.filter(id = id)
        if course.exists():
            course.update(name = data['name'], date_created = data['date_created'])
            return Response({
                "status": "success",
                "info": "Data Updated Successfully"
            })
        else:
            return Response({
                "status": "failure",
                "info": "Course Not Found"
            })
    else:
        return Response({
            "status": "failure",
            "info": serializer.errors
        })