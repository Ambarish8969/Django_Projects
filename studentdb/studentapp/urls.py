from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='studentlist'),
    path('addstudent/',views.addStudent,name='add-student'),
    path('updatestudent/<int:id>',views.updateStudent,name='update-student'),
    path('getstudent/<int:id>',views.getStudentById,name='get-student'),
    path('deletestudent/<int:id>',views.deleteStudent,name='delete-student'),
    path('deleteallstudents',views.deleteAllStudents,name='delete-all-students'),   
]