from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff
from .serializer import StaffSerializer

@api_view(['GET'])
def get_staff_all(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_staff(request, id):
    staff = Staff.objects.get(id=id)
    serializer = StaffSerializer(staff)
    return Response(serializer.data)

@api_view(['POST'])
def post_staff(request):
    data = request.data
    serializer = StaffSerializer(data = data)
    if serializer.is_valid():
        username = data['user_name']
        staff = Staff.objects.filter(user_name = username)
        if staff.exists():
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
def edit_staff(request, id):
    data = request.data
    serializer = StaffSerializer(data = data)
    if serializer.is_valid():
        staff = Staff.objects.filter(id = id)
        if staff.exists():
            staff.update(name= data['name'], surname= data['surname'], user_name= data['user_name'], password= data['password'])
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
def disable_staff(request, id):
    staff = Staff.objects.filter(id = id)
    if staff.exists():
        staff.update(disabled = True)
        return Response({
                "status": "success",
                "info": "Staff Disabled"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Staff dose not exists"
            })


@api_view(['GET'])
def enable_staff(request, id):
    staff = Staff.objects.filter(id = id)
    if staff.exists():
        staff.update(disabled = False)
        return Response({
                "status": "success",
                "info": "Staff Enabled"
            })
    else:
        return Response({
                "status": "failure",
                "info": "Staff dose not exists"
            })
