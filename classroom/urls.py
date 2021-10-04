from django.urls import path
from . import views
urlpatterns = [
  path('create/',views.createClassroom,name='createclassroom'),
  path('search-class/',views.classSearch,name='classSearch'),
]