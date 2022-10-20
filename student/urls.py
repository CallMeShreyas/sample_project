from django.urls import path
from . import views



urlpatterns = [
    path('get/<int:id>/', views.get_student, name = "GET student data"),
    path('get/', views.get_student_all, name = "GET student data of all students"),
    path('post/', views.post_student, name = "POST student data"),
    path('put/<int:id>/', views.edit_student, name = "Edit student data"),
    path('disable/<int:id>/', views.disable_student, name = "Disabl student"),
    path('enable/<int:id>/', views.enable_student, name = "Disabl student")
]
