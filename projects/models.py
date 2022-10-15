from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    completion = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length = 50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    points = models.IntegerField()
    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    completion = models.BooleanField(default=False)
    points = models.IntegerField(default=5)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        