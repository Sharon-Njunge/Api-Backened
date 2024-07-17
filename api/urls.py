from django.urls import path, include
from .views      import StudentListView, ClassesListView, ClassPeriodListView, CoursesListView, TeacherListView

urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view') ,  
    path('classe/', ClassesListView.as_view(), name = 'classes_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name = 'classperiod_list_view'),
    path('courses/', CoursesListView.as_view(), name = 'courses_list_view'),
    path('classperiod/', TeacherListView.as_view(), name = 'teacher_list_view'),
]