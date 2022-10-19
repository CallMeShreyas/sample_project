from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'
        
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'
        # exclude = ['test_related']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'
