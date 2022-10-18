from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_course_all, name = "Get courses"),
    path('get/<int:id>/', views.get_course, name = "Get corse"),
    path('post/', views.post_course, name = "POST course"),
    path('put/<int:id>/', views.put_course, name = "EDIT course")
]