from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer
from classe.models import Classes
from .serializers import  ClassesSerializer
from classperiod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from courses.models import Courses
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status
from django.utils import timezone
from datetime import timedelta




class ClassesDetailView(APIView):
    def get(self, request, id):
        classe = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classe)
        return Response(serializer.data)
    def put(self, request, id):
        classe = Classes.objects.get(id=id)
        serializer = ClassesSerializer(classe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        classe = Classes.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def post(self, request, id):
        classe = Classes.objects.get(id=id)
        action = request.data.get("action")
        if action == "add_student":
            student_id = request.data.get("student")
            student = Student.objects.get(id=student_id)
            classe.students.add(student)
            return Response({"status": "student added"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class CoursesDetailView(APIView):
    def get(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    def put(self, request, id):
        course = Courses.objects.get(id=id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    def post(self, request, id):
        course = Courses.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_teacher":
            teacher_id = request.data.get("teacher")
            teacher = Teacher.objects.get(id=teacher_id)
            course.teachers.add(teacher)
            return Response({"status": "teacher assigned"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)

class ClassesDetailView(APIView):
    def post(self, request, id):
        classe = Classes.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_teacher":
            teacher_id = request.data.get("teacher")
            teacher = Teacher.objects.get(id=teacher_id)
            classe.teachers.add(teacher)
            return Response({"status": "teacher assigned"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period)
        return Response(serializer.data)
    def put(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class WeeklyTimetableView(APIView):
    def get(self, request):
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
       
        timetable_data = {
            "start_of_week": start_of_week.isoformat(),
            "end_of_week": end_of_week.isoformat(),
        }
        return Response(timetable_data, status=status.HTTP_200_OK)