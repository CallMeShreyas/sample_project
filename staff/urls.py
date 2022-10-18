from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.get_staff, name = "GET Staff info"),
    path('post/', views.post_staff, name="POST Staff data"),
    path('put/<int:id>/', views.edit_staff, name="Edit Staff Data"),
    path('disable/<int:id>/', views.disable_staff, name = "Disabl student"),
    path('enable/<int:id>/', views.enable_staff, name = "Disabl student")
]
