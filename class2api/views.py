from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from .serializers import  StudentSerializer

class ClassesListView(APIView):
    def get(self,  request):
        Classes = Classes.objects.all()
        serializer = ClassesSerializer(Students, many=True)

        return Response(serializer.data)
