from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'
        