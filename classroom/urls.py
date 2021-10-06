from django.urls import path
from . import views
urlpatterns = [
  path('create/',views.createClassroom,name='createclassroom'),
  path('search-class/',views.classSearch,name='classSearch'),
  path('joinclass/<int:id>/',views.joinClass,name='joinclass'),
  path('courseDetails/<int:id>/',views.courseDetails,name='courseDetails'),
  path('accept/<int:id>/',views.accept,name='accept'),
]