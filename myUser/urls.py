from django.urls import path
from . import views
urlpatterns = [
  path('signup/teacher/',views.signuTeacher,name='signupteacher'),
  path('signup/student/',views.signupStudent,name='signupstudent'),
  path('signin/',views.signin,name='signin'),
  path('logout/',views.signout,name='logout'),
  path('student/dashboard/',views.studentDashboard,name='studentDashboard'),
  path('teacher/dashboard/',views.teacherDashboard,name='teacherDashboard'),
]