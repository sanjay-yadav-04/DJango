from rest_framework import serializers
from .models import Data,Student
class DataSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    contact=serializers.IntegerField()
    age=serializers.IntegerField()

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields="__all__"
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"