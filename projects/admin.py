from django.contrib import admin
from .models import Project, Manager, Employee, Task

# Register your models here.
admin.site.register(Project)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Task)