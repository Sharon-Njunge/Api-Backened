from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from student.models import Student
from classe.models import Classes
from classperiod.models import ClassPeriod
from courses.models import Courses
from teacher.models import Teacher
from .serializers import (
    StudentSerializer, MinimalStudentSerializer,
    ClassesSerializer, MinimalClassesSerializer,
    ClassPeriodSerializer, MinimalClassPeriodSerializer,
    CoursesSerializer, MinimalCoursesSerializer,
    TeacherSerializer, MinimalTeacherSerializer
)


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = MinimalStudentSerializer(students, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)  
        return Response(serializer.data)

    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def enroll_student(self, student, course_id):
        course = Courses.objects.get(id=course_id)
        student.courses.add(course)


class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = MinimalClassesSerializer(classes, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classe = Classes.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(class_periods, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = ClassPeriod.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoursesListView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = MinimalCoursesSerializer(courses, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)  
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
