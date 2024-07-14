from rest_framework import serializers
from student.models import Student

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"