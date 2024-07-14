from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from teacher.models import Teacher
from .serializers import TeacherSerializer

class TeacherListView(APIView):
    def get(self, request):
        Teacher = Teacher.objects.all()
        serializer = TeacherSerializer(Teacher, many = True)

        return Response(serializer.data)

