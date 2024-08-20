from rest_framework import serializers
from student.models import Student
from classe.models import Classes
from classperiod.models import ClassPeriod
from courses.models import Courses
from teacher.models import Teacher

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class MinimalCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["id", "name"]

class ClassesSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True)

    class Meta:
        model = Classes
        fields = "__all__"

class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["id", "name"]

class ClassPeriodSerializer(serializers.ModelSerializer):
    classe = ClassesSerializer()  

    class Meta:
        model = ClassPeriod
        fields = "__all__"

class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ["id", "start_time", "end_time"]

class StudentSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True)  

    class Meta:
        model = Student
        fields = "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = Student
        fields = ["full_name", "email"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name"]
