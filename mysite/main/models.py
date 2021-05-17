from django.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here. (relation for database)

# todo list object containing item objects
class ToDoList(models.Model):
    #related_name is name when accessing from related object(user)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
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
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    creator = models.CharField(max_length=200)
    date_created = DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

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
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_updated = timezone.now()
        return super(Issue, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.date_created)
        #return self.type
