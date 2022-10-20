from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer

@api_view(['GET'])
def get_student(request,roll):
    student = Student.objects.filter(rollno = roll)
    if student.exists():
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    else:
        return Response({
                "status": "failure",
                "info": "rollno dose not exits"
            })

@api_view(['GET'])
def get_student_all(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = data)
    if serializer.is_valid():
        username = data['user_name']
        student = Student.objects.filter(user_name = username)
        if student.exists():
            return Response({
                "status": "failure",
                "info": "Username already exists"
            })
        serializer.save()
        return Response({
            "status": "success",
            "info": "Data saved successfully"
        })

    return Response({
        "status": "failure",
        "info": serializer.errors
    })

@api_view(['PUT'])
def edit_student(request, id):
    data = request.data
    serializer = StudentSerializer(data = data)
    if serializer.is_valid():
        student = Student.objects.filter(id=id)
        if student.exists():
        # if not student:
            student.update(name= data['name'], surname= data['surname'], user_name= data['user_name'], password= data['password'])
            return Response({
                "status": "success",
                "info": "Data updated successfully"
            })
        else:
            return Response({
                "status": "failure",
                "info": "Roll number not found"
            })
    else:
        return Response({
            "status": "failure",
            "info": serializer.errors
        })

@api_view(['GET'])
def disable_student(request, roll):
    student = Student.objects.filter(rollno = roll)
    if student.exists():
        student.update(disabled = True)
        return Response({
                "status": "success",
                "info": "Student Disabled"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Student dose not exists"
            })

@api_view(['GET'])
def enable_student(request, roll):
    student = Student.objects.filter(rollno = roll)
    if student.exists():
        student.update(disabled = False)
        return Response({
                "status": "success",
                "info": "Student Enabled"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Student dose not exists"
            })