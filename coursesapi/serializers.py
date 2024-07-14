from rest_framework import serializers
from teacher.models import Teacher


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
