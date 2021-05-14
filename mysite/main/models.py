from django.db import models
from django.contrib.auth.models import User

# Create your models here. (relation for database)

# todo list object containing item objects
class ToDoList(models.Model):
    #related_name is name when accessing from related object(user)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):  # override built in toString
        return self.name

# element of todolist
class Item(models.Model):
    # create item_set for each ToDoList
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Project(models.Model):
    pass

class Issue(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type = models.CharField(
        max_length = 4,
        choices = (
            ("task", "task"),
            ("bug", "bug"),
        ),
        default = "task"
    )
    priority = models.CharField(
        max_length = 7,
        choices = (
            ("blocker", "blocker"),
            ("major", "major"),
            ("minor", "minor"),
        ),
        default = "minor"
    )
    status = models.CharField(
        max_length = 11,
        choices = (
            ("assigned", "assigned"),
            ("in-progress", "in-progress"),
            ("resolved", "resolved"),
        ),
        default = "assigned"
    )
    creator = models.CharField(max_length=200)
    assignee = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
