from django.urls import path, include
from .views      import StudentListView

urlpatterns = [
    path('class/', StudentListView.as_view(), name = 'classes_list_view')
]