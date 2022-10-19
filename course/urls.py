from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_course_all, name = "Get courses"),
    path('get/<int:id>/', views.get_course, name = "Get corse"),
    path('post/', views.post_course, name = "POST course"),
    path('put/<int:id>/', views.put_course, name = "EDIT course"),
    path('get/test/', views.get_test_all, name = "GET tests"),
    path('get/<int:course_id>/test/<int:test_id>/', views.get_test, name = "GET test "),
    path('post/<int:course_id>/', views.post_test, name = "POST test related to the course"),
    path('post/<int:course_id>/all/', views.post_test_for_all, name = "POST test related to the course"),
    path('get/question/<int:question_id>/', views.get_question, name = "GET question"),
    path('post/<int:course_id>/<slug:test_name>/', views.post_question, name = "POST question")
]