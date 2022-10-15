from django.urls import path
from . import views

urlpatterns = [
    path('employees/',views.employees, name = "employees"),
    path('employees/<int:employee_id>',views.employee,name='employee'),
    path('projects/', views.projects, name = "projects"),
    path('projects/<int:project_id>', views.project, name = "project"),
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("", views.dashboard, name = "dashboard"),
]