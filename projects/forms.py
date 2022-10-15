from django.forms import ModelForm
from .models import Project, Task, Employee


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name','description','start_date','end_date']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','start_date','end_date', 'project', 'employee', 'points']

        