from datetime import date
# from sqlite3 import Date
from django.shortcuts import render
from .models import Employee, Project, Task
from .forms import ProjectForm, TaskForm

# Create your views here.
def employees(request):
    employees=Employee.objects.all()
    durations = []
    for employee in employees:
        tasks = employee.task_set.all()
        max_ = date.today()
        for task in tasks:
            if not task.completion:
                max_ = max(max_, task.end_date)

        # if max_ == date.today():
        #     max_ = 0

        durations.append([employee, max_])

    durations.sort(key=lambda item: item[1])
    for duration in durations:
        if duration[1]==date.today():
            max_=0
    return render(request, 'projects/employees.html', {
        'employees': employees,
        'durations': durations,
    })

def employee(request,employee_id):
    employee=Employee.objects.get(pk=employee_id)
    tasks=employee.task_set.all()
    projects=set()
    for task in tasks:
        project=task.project
        projects.add(project)  
        
    return render(request,'projects/employee.html',{
        'employee':employee,
        'projects':projects,
        'tasks':tasks
    })    

def projects(request):
    if request.method == 'POST':
        list_of_input_ids=request.POST.getlist('inputs')
        if len(list_of_input_ids) !=0:
            for id in list_of_input_ids:
                id=int(id)
                project=Project.objects.get(pk=id)
                project.completion=True
                project.save()
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # save the form data to model
            form.save()
    projects = Project.objects.all()
    list = []
    for project in projects:
        complete = 0
        incomplete = 0
        tasks = project.task_set.all()
        for task in tasks:
            if(task.completion == True):
                complete += 1
            else:
                incomplete += 1
        list.append([project,complete,incomplete])
    
    return render(request,'projects/projects.html',{
        'list': list,
        'form':ProjectForm()
    })

def project(request, project_id):
    if request.method == 'POST':
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # save the form data to model
            form.save()
    project = Project.objects.get(pk = project_id)
    tasks = project.task_set.all()
    # employees = set()
    # for task in tasks:
    #     employees.add(task.employee)
    # employees = list(employees)
    return render(request,'projects/project.html',{
        'project':project,
        'tasks':tasks,
        'form':TaskForm()
    })

def dashboard(request):
    projects = Project.objects.all()
    projects = sorted(projects,key=lambda x : x.end_date)
    incompleted_projects = 0
    for project in projects:
        if(project.completion == False):
            incompleted_projects += 1
    top_5_incompleted_projects = []
    for project in projects:
        if(project.completion == False):
            top_5_incompleted_projects.append(project)
        if(len(top_5_incompleted_projects) >= 5):
            break
    #################################
    min_ = date(2100, 5, 17)
    outdated_project = ''
    for project in projects:
        if(project.start_date < min_ and project.completion == False):
            min_ = min(min_, project.end_date)
            outdated_project = project.name
    #####################################
    employees = Employee.objects.all()
    max_points = -100
    for employye in employees:
        if(employye.points > max_points):
            max_points = employye.points
            max_employye = employye.name
    #####################################
    employees=Employee.objects.all()
    durations = []
    for employee in employees:
        tasks = employee.task_set.all()
        max_ = date.today()
        for task in tasks:
            if not task.completion:
                max_ = max(max_, task.end_date)

        # if max_ == date.today():
        #     max_ = 0

        durations.append([employee, max_])

    durations.sort(key=lambda item: item[1])
    for duration in durations:
        if duration[1]==date.today():
            max_=0
    return render(request,'projects/dashboard.html',{
        'incompleted_projects': incompleted_projects,
        'most_urgent_date':min_,
        'outdated_project': outdated_project,
        'most_points': max_points,
        'max_points_employee':max_employye,
        "top_5_incompleted_projects": top_5_incompleted_projects,
        'durations':durations
    })
    # employees = Employee.objects.all()
    # durations=[]
    # for employee in employees:
    #     tasks = employee.task_set.all()
    #     max_ = date.today()
    #     for task in tasks:
    #         max_ = max(max_, task.end_date)
    #     durations.append([employee.name,max_])
    # projects = Project.objects.all()
    # list = []
    # for project in projects:
    #     arr = []
    #     arr.append(project.name)
    #     complete = 0
    #     incomplete = 0
    #     tasks = project.task_set.all()
    #     for task in tasks:
    #         if(task.completion == True):
    #             complete += 1
    #         else:
    #             incomplete += 1
    #     arr.append(complete)
    #     arr.append(incomplete)
    #     list.append(arr)
    # return render(request,'projects/dashboard.html',{
    #     'list':list,
    #     'durations':durations
    # })

def employee_dashboard(request, employee_id):
    employee=Employee.objects.get(pk=employee_id)
    tasks=employee.task_set.all()
    if request.method == 'POST':
        list_of_input_ids=request.POST.getlist('inputs')
        for id in list_of_input_ids:
            id=int(id)
            task=Task.objects.get(pk=id)
            task.completion=True
            task.save()
    points=0    
    employee=Employee.objects.get(pk=employee_id)
    tasks=employee.task_set.all()
    for task in tasks:
        if task.completion:
            points+=task.points
    employee.points=points
    employee.save()
    projects=set()
    for task in tasks:
        project=task.project
        projects.add(project)  
    id = request.POST.get('docid')
    return render(request,'projects/employee_dashboard.html',{
        'employee':employee,
        'projects':projects,
        'tasks':tasks
    })
