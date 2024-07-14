from django.urls import path, include
from .views   import TeacherListView

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name = 'courses_list_view')
]


