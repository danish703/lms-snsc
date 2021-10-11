from django.urls import path
from . import views
urlpatterns=[
    path('details/<int:id>',views.assignment,name='assignment'),
    path('edit/<int:id>',views.assignmentEdit,name='assignmentEdit'),
    path('del/<int:id>',views.assignmentDel,name='assignmentDel'),
]