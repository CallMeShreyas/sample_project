from rest_framework import serializers
from .models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        # fields = ('name', "surname", 'user_name', 'password')
        fields = '__all__'
        