from rest_framework.decorators import api_view
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , User
from django.http import JsonResponse
from rest_framework.response import Response
from student.models import Student
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


@api_view(['GET'])
def get_test_all(request):
    test = Test.objects.all()
    serializer = TestSerializer(test, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_test(request, test_id, course_id):
    course = Course.objects.filter(id = course_id)
    if course.exists():
        test = Test.objects.filter(id = test_id)
        if test.exists():
            if test[0].course_related.id == course_id:
                serializer = TestSerializer(test, many = True)
                return Response(serializer.data)
            else:
                print(test[0].course_related.id)
                return Response({
                    "status": "failure",
                    "info": "Test not found for this course"
                })
        else:
            return Response({
                "status": "failure",
                "info": "Test dose not exists"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Course dose not exists"
            })

@api_view(['POST'])
def post_test(request, course_id):
    data = request.data
    data['course_related'] = course_id
    serializer = TestSerializer(data = data)
    course = Course.objects.filter(id = course_id)
    if course.exists():
        student = Student.objects.filter(id = data['given_to'])
        if student.exists():
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "info": "Test added successfully"
                })
            else:
                return Response({
                    "status": "failure",
                    "info": serializer.errors
                })
        else:
            return Response({
                "status": "failure",
                "info": "Student dose not exists"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Course dose not exists"
            })

@api_view(['POST'])
def post_test_for_all(request, course_id):
    data = request.data
    serializer = TestSerializer(data=data)
    if serializer.is_valid():
        student = Student.objects.all()
        for i in student:
            data['given_to'] = i.id
            serializer = TestSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        return Response({
            "status": "success",
            "info": "Test assigned to all students"
        })
    else:
        return Response({
            "status": "failure",
            "info": serializer.errors
        })

@api_view(['GET'])
def get_question(request, question_id):
    question = Question.objects.filter(id = question_id)
    if question.exists():
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
    return Response({
        "status": "failure",
        "info": "question dose not exists"
    })

@api_view(['POST'])
def post_question(request, course_id, test_name):
    data = request.data
    test = Test.objects.filter(name = test_name)
    print(test[0].id)
    if test.exists():
        for i in test:
            data['test_related'] = i.id
            print(data)
            serializer = QuestionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({
                    "status": "failure",
                    "info": serializer.errors
                })
        return Response({
            "status": "success",
            "info": "Question added successfully"
            })
    else:
        return Response({
            "status": "failure",
            "info": "test dose not exists"
        })