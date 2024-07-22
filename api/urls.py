from django.urls import path, include
from .views      import StudentListView, ClassesListView, ClassPeriodListView, CoursesListView, TeacherListView, StudentDetailView, TeacherDetailView, CoursesDetailView, ClasesDetailView, ClassPeriodDetailView


urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view') ,  
    path('classe/', ClassesListView.as_view(), name = 'classes_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name = 'classperiod_list_view'),
    path('courses/', CoursesListView.as_view(), name = 'courses_list_view'),
    path('teacher/', TeacherListView.as_view(), name = 'teacher_list_view'),
    path('student/<int:id>/', StudentDetailView.as_view(), name ='student_detail_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name ='teacher_detail_view'),
    path('courses/<int:id>/', CoursesDetailView.as_view(), name ='courses_detail_view'),
    path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name ='classperiod_detail_view'),
    path('classe/<int:id>/', ClasesDetailView.as_view(), name ='classes_detail_view'),  
]