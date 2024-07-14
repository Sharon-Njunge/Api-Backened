from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Teacher
from .serializers import CoursesSerializer

class CoursesListView(APIView):
    def get(self, request):
        Courses = Courses.objects.all()
        serializer = CoursesSerializer(Courses, many = True)

        return Response(serializer.data)

